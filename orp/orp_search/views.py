import logging

from orp_search.public_gateway import PublicGateway, SearchDocumentConfig

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.forms import RegulationSearchForm

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def details(request: HttpRequest, id) -> HttpResponse:
    """Details view.

    Handles the GET request to fetch details based on the provided id.
    """

    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    # Extract the id parameter from the request
    document_id = id
    logger.info("document id: %s", document_id)
    if not document_id:
        context["error"] = "no document id provided"
        return render(request, template_name="details.html", context=context)

    # Create a SearchDocumentConfig instance and set the id parameter
    config = SearchDocumentConfig(search_terms="", dummy=True, id=document_id)

    # Use the PublicGateway class to fetch the details
    public_gateway = PublicGateway()
    try:
        search_result = public_gateway.search(config)
        logger.info("search result: %s", search_result)

        if "regulatory_topics" in search_result:
            search_result["regulatory_topics"] = search_result[
                "regulatory_topics"
            ].split("\n")

        context["result"] = search_result
        return render(request, template_name="details.html", context=context)
    except Exception as e:
        logger.error("error fetching details: %s", e)
        context["error"] = f"error fetching details: {e}"
        return render(request, template_name="details.html", context=context)


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
    limit = form.cleaned_data.get("limit", 10)
    offset = form.cleaned_data.get("page", 1)

    # If the search query is empty, return the form
    if not search_query:
        logger.info("no search query provided")
    else:
        logger.info("search query: %s", search_query)

    logger.info("document types: %s", document_types)
    logger.info("page: %s", offset)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(
        search_query, document_types, dummy=True, limit=limit, offset=offset
    )

    # Check if the response is cached
    public_gateway = PublicGateway()
    search_results = public_gateway.search(config)
    context["results_count_total"] = len(search_results)

    # search_results contains too much information for the
    # landing page (search) so we need to filter it and
    # reduce the amount of information to be displayed
    # on the landing page.

    if search_results:
        paginated_search_results = public_gateway.paginate_results(
            config, search_results
        )
        logger.info(
            "paginated search results after paginate: %s",
            paginated_search_results,
        )

        # We can use the following code to filter the search_results list:
        paginated_search_results = [
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
                "regulatory_topics": " | ".join(
                    result["regulatory_topics"].split("\n")
                ),
            }
            for result in paginated_search_results
        ]
        context["results_count"] = len(paginated_search_results)
    else:
        paginated_search_results = []

    context["results"] = paginated_search_results
    context["results_count"] = len(paginated_search_results)
    context["results_page_total"] = public_gateway.calculate_total_pages(
        config, context["results_count_total"]
    )

    logger.info("search results: %s", context["results"])
    logger.info("search results count: %s", context["results_count"])
    logger.info(
        "search results total count: %s", context["results_count_total"]
    )
    logger.info("search results page total: %s", context["results_page_total"])
    logger.debug("paginated search results: %s", paginated_search_results)
    return render(request, template_name="orp.html", context=context)
