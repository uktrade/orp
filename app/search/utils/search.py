# flake8: noqa
# isort: skip_file

import logging
import re
import time

from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)  # noqa
from django.db.models import F, Func, Q, QuerySet
from django.http import HttpRequest

from app.search.config import SearchDocumentConfig
from app.search.models import DataResponseModel
from app.search.utils.paginate import paginate
from app.search.utils.terms import sanitize_input

logger = logging.getLogger(__name__)


def create_search_query(search_string):
    """
    Create a search query from a search string with
    implicit AND for space-separated words
    and explicit AND/OR operators.

    :param search_string: The search string to parse
    :return: A combined SearchQuery object
    """
    # Split the string into tokens, handling quoted phrases and operators
    tokens = re.findall(r'"[^"]+"|\bAND\b|\bOR\b|\w+', search_string)

    # Validate tokens to avoid issues with syntax
    if not tokens:
        return None  # Return None for empty or invalid input

    # Initialize variables
    query = None
    current_operator = "&"  # Default to implicit AND for space-separated words

    # Process tokens
    for token in tokens:
        if token.upper() == "AND":
            current_operator = "&"
        elif token.upper() == "OR":
            current_operator = "|"
        else:
            # Handle phrases and plain text
            is_phrase = token.startswith('"') and token.endswith('"')
            clean_token = token.strip('"')
            new_query = SearchQuery(
                clean_token, search_type="phrase" if is_phrase else "plain"
            )

            # Combine queries based on the current operator
            if query is None:
                query = new_query  # First token initializes the query
            else:
                if current_operator == "&":
                    query = query & new_query
                elif current_operator == "|":
                    query = query | new_query

            # Reset the operator to implicit AND for the next token
            current_operator = "&"

    return query


def search_database(
    config: SearchDocumentConfig,
):
    """
    Search the database for documents based on the search query.

    :param config: The search configuration object
    :return: A QuerySet of DataResponseModel objects
    """
    queryset = DataResponseModel.objects.all()

    # Filter by ID if provided
    if config.id:
        try:
            return DataResponseModel.objects.get(id=config.id)
        except DataResponseModel.DoesNotExist:
            return DataResponseModel.objects.none()

    # Sanitize and process the search query
    query_str = sanitize_input(config.search_query)
    if not query_str:
        return DataResponseModel.objects.none()

    # Generate the search query using the updated create_search_query function
    search_query = create_search_query(query_str)
    if not search_query:
        return DataResponseModel.objects.none()

    # Annotate with SearchVector for ranking
    vector = SearchVector("title", "description", "regulatory_topics")
    queryset = queryset.annotate(rank=SearchRank(vector, search_query))

    # Combine full-text search and partial matches
    partial_matches = (
        Q(title__icontains=query_str)
        | Q(description__icontains=query_str)
        | Q(regulatory_topics__icontains=query_str)
    )
    queryset = queryset.filter(Q(search=search_query) | partial_matches)

    # Filter by document types if provided
    if config.document_types:
        queryset = queryset.filter(type__in=config.document_types)

    # Filter by publishers if provided
    if config.publisher_names:
        queryset = queryset.filter(publisher_id__in=config.publisher_names)

    # Sort results based on the sort_by parameter
    if config.sort_by == "relevance":
        return queryset.order_by("-rank")
    return queryset.order_by("-sort_date")


def search(
    context: dict, request: HttpRequest, ignore_pagination=False
) -> dict | QuerySet[DataResponseModel]:
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

    if ignore_pagination:
        return results

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
