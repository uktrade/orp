import logging
import re
import time

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel
from orp_search.utils.documents import calculate_score
from orp_search.utils.paginate import paginate
from orp_search.utils.terms import sanitize_input

from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import QuerySet
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


def _search_database(
    config: SearchDocumentConfig,
) -> QuerySet[DataResponseModel]:
    # Sanatize the query string
    query_str = sanitize_input(config.search_query)

    # Generate query object
    query_objs = _create_search_query(query_str)

    # Search across specific fields
    vector = SearchVector("title", "description")

    # Filter results based on document types if provided
    queryset = DataResponseModel.objects.annotate(search=vector).filter(
        search=query_objs,
        **(
            {"type__in": config.document_types}
            if config.document_types
            else {}
        ),
    )

    # Sort results based on the sort_by parameter
    if config.sort_by == "recent":
        return queryset.order_by("-date_modified")

    if config.sort_by == "relevance":
        calculate_score(config, queryset)
        return queryset.order_by("score")


def search(context: dict, request: HttpRequest) -> dict:
    logger.info("received search request: %s", request)
    start_time = time.time()

    search_query = request.GET.get("search", "")
    document_types = request.GET.get("document_type", "").lower().split(",")
    offset = request.GET.get("page", "1")
    offset = int(offset) if offset.isdigit() else 1
    limit = request.GET.get("limit", "10")
    limit = int(limit) if limit.isdigit() else 10
    publisher = request.GET.getlist("publisher", None)
    sort_by = request.GET.get("sort", None)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(
        search_query,
        document_types,
        limit=limit,
        offset=offset,
        publisher_names=publisher,
        sort_by=sort_by,
    )

    # Display the search query in the log
    config.print_to_log()

    # Search across specific fields
    results = _search_database(config)

    # convert search_results into json
    pag_start_time = time.time()
    context = paginate(context, config, results)
    pag_end_time = time.time()

    logger.info(
        f"time taken to paginate (called from views.py): "
        f"{round(pag_end_time - pag_start_time, 2)} seconds"
    )

    end_time = time.time()
    logger.info(
        f"time taken to search and produce response: "
        f"{round(end_time - start_time, 2)} seconds"
    )

    return context
