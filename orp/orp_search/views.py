import logging

from orp_search.models import PublicGatewayCache
from orp_search.public_gateway import PublicGateway, SearchDocumentConfig

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.forms import RegulationSearchForm

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def search(request: HttpRequest) -> HttpResponse:
    """Search view.

    Handles the search functionality and renders the search page. This view
    function processes GET requests for the search page. It displays the search
    form and, if a valid search query is provided, shows the search results.
    The search results are fetched from the DBT Data API. If an error occurs
    during the Data API search, the service problem page is displayed.
    """

    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    # Create a new instance of the RegulationSearchForm
    form = RegulationSearchForm(request.GET or None)

    # If the form is not valid, return the form
    if not form.is_valid():
        return render(request, template_name="orp.html", context=context)

    # Add the form to the context
    context["form"] = form

    # Get the search query and document types from the form
    search_query = form.cleaned_data.get("query")
    document_types = form.cleaned_data.get("document_type")

    # If the search query is empty, return the form
    if not search_query:
        # Then we just get all results but only return a
        # few based on limit, default is 10
        logger.info("no search query provided")
    else:
        logger.info("search query: %s", search_query)

    logger.info("Document types: %s", document_types)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(search_query, document_types, dummy=True)

    # Check if the response is cached
    logger.info("checking for cached response")

    cached_response = PublicGatewayCache.get_cached_response(config)
    if cached_response:
        logger.info("reusing cached response")
        search_results = cached_response
    else:
        logger.info("fetching new response")
        public_gateway = PublicGateway()
        search_results = public_gateway.search(config)

        # Cache the response
        logger.info("caching response")
        PublicGatewayCache.cache_response(config, search_results)

        logger.info("using cached response")
        search_results = PublicGatewayCache.get_cached_response(config)

        logger.info("cached response results: %s", search_results)

    # search_results contains too much information for the
    # landing page (search) so we need to filter it and
    # reduce the amount of information to be displayed
    # on the landing page.

    # For each item in search_results, we only need the following:
    # - id
    # - title
    # - publisher
    # - description (only keep the first 100 words)
    # - date_issued
    # - date_modified

    # We can use a list comprehension to filter the search_results
    # list and only keep the required information.

    # We can use the following code to filter the search_results list:
    search_results = [
        {
            "id": result["id"],
            "title": result["title"],
            "publisher": result["publisher"],
            "description": (
                result["description"][:100] + "..."
                if len(result["description"]) > 100
                else result["description"]
            ),
            "date_issued": result["date_issued"],
            "date_modified": result["date_modified"],
            "document_type": result["type"],
            "regulatory_topics": result["regulatory_topics"],
        }
        for result in search_results
    ]

    context["results"] = search_results
    context["results_count"] = len(search_results)
    logger.info("search results: %s", search_results)
    logger.info("search results count: %s", len(search_results))
    return render(request, template_name="orp.html", context=context)


@require_http_methods(["GET"])
def details(request: HttpRequest) -> HttpResponse:
    """Regulation details.

    Returns regulation details page.
    """
    context = {
        "service_name": settings.SERVICE_NAME,
    }
    return render(request, template_name="details.html", context=context)
