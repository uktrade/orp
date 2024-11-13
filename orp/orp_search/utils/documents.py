import re

from numpy.f2py.auxfuncs import throw_error
from orp_search.models import DataResponseModel, logger

from django.db.models import QuerySet


def clear_all_documents():
    logger.info("clearing all documents from table...")
    try:
        DataResponseModel.objects.all().delete()
        logger.info("documents cleared from table")
    except Exception as e:
        logger.error(f"error clearing documents: {e}")
        throw_error(f"error clearing documents: {e}")


def insert_or_update_document(document_json):
    try:
        logger.info("creating document...")
        logger.debug(f"document: {document_json}")
        # Try to create a new document
        document = DataResponseModel.objects.create(**document_json)
    except Exception as e:
        logger.error(f"error creating document: {document_json}")
        logger.error(f"error: {e}")
        logger.info("document already exists, updating...")

        # If a duplicate key error occurs, update the existing document
        document = DataResponseModel.objects.get(pk=document_json["id"])
        for key, value in document_json.items():
            setattr(document, key, value)
        document.save()
        logger.info(f"document updated: {document}")


def calculate_score(config, queryset: QuerySet):
    """
    Calculate the score of a search result based on the number of
    search terms found in the title and description.

    :param search_terms: A list of search terms to look for in the
                         search result.
    :return: The score based on the number of search terms found.
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
