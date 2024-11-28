import base64
import re
import uuid

from numpy.f2py.auxfuncs import throw_error

from django.db.models import QuerySet

from search.models import DataResponseModel, logger


def clear_all_documents():
    """
    Clears all documents from the 'DataResponseModel' table in the database.

    Logs the process of clearing the documents and handles any exceptions
    that may occur. If an error occurs, it logs the error message and
    raises an error.

    Raises:
        CustomError: If there is an error while clearing the documents.
    """
    logger.debug("clearing all documents from table...")
    try:
        DataResponseModel.objects.all().delete()
        logger.debug("documents cleared from table")
    except Exception as e:
        logger.error(f"error clearing documents: {e}")
        throw_error(f"error clearing documents: {e}")


def insert_or_update_document(document_json):
    """
    Inserts or updates a database document based on the given JSON data.

    The function first attempts to create a new document using the
    provided JSON data.

    If the document already exists (detected through an exception),
    it catches the error and tries to update the existing document instead.

    Args:
        document_json (dict): A dictionary containing the data for the
        document to be inserted or updated.

    Raises:
        Exception: If an error occurs during either the insert or update
        operation, the error is logged and re-raised.

    Logs:
        Logs detailed debug messages for each step, including the document
        being inserted, any errors encountered, and the outcome of the update
        operation.
    """
    try:
        logger.debug("creating document...")
        logger.debug(f"document: {document_json}")
        document = DataResponseModel(**document_json)
        document.full_clean()
        document.save()
    except Exception as e:
        logger.error(f"error creating document: {document_json}")
        logger.error(f"error: {e}")
        logger.debug("document already exists, updating...")

        # If a duplicate key error occurs, update the existing document
        try:
            document = DataResponseModel.objects.get(pk=document_json["id"])
            for key, value in document_json.items():
                setattr(document, key, value)
            document.save()
            logger.debug(f"document updated: {document}")
        except Exception as e:
            logger.error(f"error updating document: {document_json}")
            logger.error(f"error: {e}")
            throw_error(f"error updating document: {document_json}")


def calculate_score(config, queryset: QuerySet):
    """
    Calculate the search relevance score for each document in the queryset.

    Args:
        config: Configuration object containing the search query settings.
        queryset: QuerySet of documents to be scored.

    The function tokenizes the search query, filters out "AND" and "OR",
    and computes the score for each document based on the frequency of
    search terms in the document's title and description.
    """

    def _extract_terms(search_query):
        # Use regex to find words and phrases, ignoring AND and OR
        tokens = re.findall(r'"[^"]+"|\b\w+\b', search_query)

        # Filter out AND and OR
        terms = [
            token.strip('"') for token in tokens if token not in ("AND", "OR")
        ]
        return terms

    search_query = config.search_query

    if not search_query:
        return

    search_query = _extract_terms(search_query)

    # Get all documents from the queryset
    documents = list(queryset)

    # Iterate over each document and calculate the score
    for document in documents:
        title = document.title or ""
        description = document.description or ""
        combined_content = title.lower() + " " + description.lower()
        document.score = sum(
            combined_content.count(term.lower()) for term in search_query
        )
        document.save()


def generate_short_uuid():
    """
    Generates a short, URL-safe UUID.

    Returns:
        str: A URL-safe base64 encoded UUID truncated to 22 characters.
    """
    uid = uuid.uuid4()

    # Encode it to base64
    uid_b64 = base64.urlsafe_b64encode(uid.bytes).rstrip(b"=").decode("ascii")
    return uid_b64[
        :22
    ]  # Shorten as needed, typically more than 22 characters are
    # unnecessary and remain unique.
