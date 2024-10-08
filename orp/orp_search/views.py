import json
import logging
import re

from orp_search.models import PublicGatewayCache
from orp_search.public_gateway import PublicGateway, SearchDocumentConfig

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.forms import RegulationSearchForm

logger = logging.getLogger(__name__)


def clean_json_response(response):
    # Ensure the response is a string
    if isinstance(response, dict):
        response = json.dumps(response)

    # Clean the escape characters and fix JSON format
    cleaned_response = response.replace('\\"', '"').replace("\\r\\n", "\n")

    # Remove invalid control characters
    # Regex to match and remove control characters except '\n' or '\t'
    cleaned_response = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", cleaned_response)

    # Split concatenated JSON objects by looking for "} {"
    json_objects = re.split(r"}\s*{", cleaned_response)

    # Add missing braces to objects
    json_objects = [
        obj if obj.strip().startswith("{") else "{" + obj
        for obj in json_objects
    ]
    json_objects = [
        obj if obj.strip().endswith("}") else obj + "}" for obj in json_objects
    ]

    # Parse each JSON object
    parsed_objects = [json.loads(obj) for obj in json_objects]

    return parsed_objects


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

    search_query_json = json.dumps(search_query)
    document_types_json = json.dumps(document_types)

    logger.info("Search query (json): %s", search_query_json)
    logger.info("Document types (json): %s", document_types_json)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(search_query, document_types)

    # Check if the response is cached
    logger.info("checking for cached response")
    cached_response = PublicGatewayCache.get_cached_response(config)
    if cached_response:
        logger.info("using cached response")
        search_results = json.loads(cached_response)
    else:
        logger.info("fetching new response")
        public_gateway = PublicGateway()
        search_results = public_gateway.search(config)
        search_results = clean_json_response(search_results)

        # Cache the response
        logger.info("caching response")
        PublicGatewayCache.cache_response(config, json.dumps(search_results))

    logger.info("search results json: %s", search_results)
    context["search_results"] = search_results
    return render(request, template_name="orp.html", context=context)
