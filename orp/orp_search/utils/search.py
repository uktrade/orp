import logging
import re
import time

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel
from orp_search.utils.documents import calculate_score
from orp_search.utils.paginate import paginate
from orp_search.utils.terms import sanitize_input

from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import F, Func, Q, QuerySet
from django.http import HttpRequest

logger = logging.getLogger(__name__)


def _create_search_query(search_string):
    """
    Create a search query from a search string with AND/OR operators

    :param search_string: The search string to parse
    :return: A SearchQuery object
    """
    # Split the string into words and phrases using a regex that
    # captures quoted text and words
    tokens = re.findall(r'"[^"]+"|\bAND\b|\bOR\b|\b\w+\b', search_string)

    # Initialize an empty query
    preprocess_query = None
    current_operator = "&"  # Default to AND

    # Iterate over tokens to build the query
    for token in tokens:
        if token == "AND":  # nosec BXXX
            current_operator = "&"  # nosec BXXX
        elif token == "OR":  # nosec BXXX
            current_operator = "|"  # nosec BXXX
        else:
            # Remove quotes if it's a phrase
            is_phrase = token.startswith('"') and token.endswith('"')
            clean_token = token.strip('"') if is_phrase else token
            search_query = SearchQuery(
                clean_token, search_type="phrase" if is_phrase else "plain"
            )

            # Combine the query based on the current operator
            if preprocess_query is None:
                preprocess_query = search_query
            else:
                if current_operator == "&":
                    preprocess_query &= search_query
                elif current_operator == "|":
                    preprocess_query |= search_query

    return preprocess_query


def search_database(
    config: SearchDocumentConfig,
) -> QuerySet[DataResponseModel]:
    """
    Search the database for documents based on the search query

    :param config: The search configuration object
    :return: A QuerySet of DataResponseModel objects
    """

    # If an id is provided, return the document with that id
    if config.id:
        return DataResponseModel.objects.filter(id=config.id)

    # Sanatize the query string
    query_str = sanitize_input(config.search_query)
    logger.debug(f"sanitized search query: {query_str}")

    # Generate query object
    query_objs = _create_search_query(query_str)
    logger.debug(f"search query objects: {query_objs}")

    # Search across specific fields
    vector = SearchVector("title", "description", "regulatory_topics")

    queryset = DataResponseModel.objects.all()

    if query_objs:
        # Treat the query for partial and full-text search
        query_chunks = query_str.split()
        search_vector = SearchVector(
            "title", "description", "regulatory_topics"
        )
        queryset = queryset.annotate(search=search_vector)

        # Creating a combined SearchQuery object from chunks
        search_queries = [
            SearchQuery(chunk, search_type="plain") for chunk in query_chunks
        ]
        combined_query = search_queries[0]
        for sq in search_queries[1:]:
            combined_query |= sq

        partial_matches = Q()
        for chunk in query_chunks:
            partial_matches |= (
                Q(title__icontains=chunk)
                | Q(description__icontains=chunk)
                | Q(regulatory_topics__icontains=chunk)
            )

        queryset = queryset.filter(partial_matches | Q(search=combined_query))
    else:
        queryset = DataResponseModel.objects.annotate(search=vector)

    # Filter by document types
    if config.document_types:
        query = Q()

        # Loop through the document types and add a Q object for each one
        for doc_type in config.document_types:
            query |= Q(type__icontains=doc_type)
        queryset = queryset.filter(query)

    # Filter by publisher
    if config.publisher_names:
        query = Q()

        # Loop through the document types and add a Q object for each one
        for publisher in config.publisher_names:
            query |= Q(publisher_id__icontains=publisher)
        queryset = queryset.filter(query)

    # Sort results based on the sort_by parameter (default)
    if config.sort_by is None or config.sort_by == "recent":
        return queryset.order_by("-sort_date")

    if config.sort_by is not None and config.sort_by == "relevance":
        # Calculate the score for each document
        calculate_score(config, queryset)
        return queryset.order_by("score")

    return queryset


def search(context: dict, request: HttpRequest) -> dict:
    logger.debug("received search request: %s", request)
    start_time = time.time()

    search_query = request.GET.get("query", "")
    document_types = request.GET.getlist("document_type", [])
    offset = request.GET.get("page", "1")
    offset = int(offset) if offset.isdigit() else 1
    limit = request.GET.get("limit", "10")
    limit = int(limit) if limit.isdigit() else 10
    publishers = request.GET.getlist("publisher", [])
    sort_by = request.GET.get("sort", None)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(
        search_query,
        document_types,
        limit=limit,
        offset=offset,
        publisher_names=publishers,
        sort_by=sort_by,
    )

    # Display the search query in the log
    config.print_to_log()

    # Search across specific fields
    results = search_database(config)

    # convert search_results into json
    pag_start_time = time.time()
    context = paginate(context, config, results)
    pag_end_time = time.time()

    logger.debug(
        f"time taken to paginate (called from views.py): "
        f"{round(pag_end_time - pag_start_time, 2)} seconds"
    )

    end_time = time.time()
    logger.debug(
        f"time taken to search and produce response: "
        f"{round(end_time - start_time, 2)} seconds"
    )

    return context


class Trim(Func):
    function = "TRIM"
    template = "%(function)s(%(expressions)s)"


def get_publisher_names():
    logger.debug("getting publisher names...")
    publishers_list = []

    try:
        publishers_list = (
            DataResponseModel.objects.annotate(
                trimmed_publisher=Trim(F("publisher")),
                trimmed_publisher_id=Trim(F("publisher_id")),
            )
            .values(
                "trimmed_publisher",
                "trimmed_publisher_id",
            )
            .distinct()
        )

    except Exception as e:
        logger.error(f"error getting publisher names: {e}")
        logger.debug("returning empty list of publishers")

    logger.debug(f"publishers found: {publishers_list}")
    return publishers_list
