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

    # r = requests.get('https://swapi.dev/api/people/1/')
    # if r.status_code == 200:
    #     logger = logging.getLogger(__name__)
    #     logger.info('Data fetched successfully', r.status_code)
    #     return HttpResponse(r.text)

    # return HttpResponse('Could not save data')

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
        return render(request, template_name="orp.html", context=context)

    logger.info("Search query: %s", search_query)
    logger.info("Document types: %s", document_types)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(search_query, document_types, dummy=True)

    # Check if the response is cached
    logger.info("checking for cached response")
    cached_response = PublicGatewayCache.get_cached_response(config)
    if cached_response:
        logger.info("using cached response")
        search_results = cached_response
    else:
        logger.info("fetching new response")
        public_gateway = PublicGateway()
        search_results = public_gateway.search(config)

        # Cache the response
        PublicGatewayCache.cache_response(config, search_results)

    logger.info("search results json: %s", search_results)
    context["results"] = search_results
    return render(request, template_name="orp.html", context=context)
