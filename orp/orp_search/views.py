import base64
import csv
import logging

import pandas as pd

from orp_search.legislation import Legislation
from orp_search.public_gateway import PublicGateway, SearchDocumentConfig
from orp_search.utils.paginate import paginate
from orp_search.utils.results import calculate_score, parse_date

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from core.forms import RegulationSearchForm

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def document(request: HttpRequest, id) -> HttpResponse:
    """Document details view.

    Handles the GET request to fetch details based on the provided id.
    """
    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    def _decode_url(encoded_url):
        decoded_bytes = base64.urlsafe_b64decode(encoded_url.encode("utf-8"))
        return decoded_bytes.decode("utf-8")

    # Extract the id parameter from the request
    document_id = id

    # Decode id to see if it's a url ?
    try:
        decoded_url = _decode_url(document_id)
        return redirect(decoded_url)
    except Exception:
        logger.info("document id is not a url")

    logger.info("document id: %s", document_id)
    if not document_id:
        context["error"] = "no document id provided"
        return render(request, template_name="document.html", context=context)

    # Create a SearchDocumentConfig instance and set the id parameter
    config = SearchDocumentConfig(search_terms="", dummy=True, id=document_id)

    # Use the PublicGateway class to fetch the details
    public_gateway = PublicGateway()
    try:
        search_result = public_gateway.search(config)
        # logger.info("search result: %s", search_result)

        if "regulatory_topics" in search_result:
            search_result["regulatory_topics"] = str(
                search_result["regulatory_topics"]
            ).split("\n")

        if "related_legislation" in search_result:
            search_result["related_legislation"] = str(
                search_result["related_legislation"]
            ).split("\n")

        context["result"] = search_result
        return render(request, template_name="document.html", context=context)
    except Exception as e:
        logger.error("error fetching details: %s", e)
        context["error"] = f"error fetching details: {e}"
        return render(request, template_name="document.html", context=context)


@require_http_methods(["GET"])
def download_search_csv(request: HttpRequest) -> HttpResponse:
    search_terms = request.GET.get("search", "")
    document_type_terms = request.GET.getlist("document_type", "")
    publisher_terms = request.GET.getlist("publisher", None)
    sort_by = request.GET.get("sort", None)

    config = SearchDocumentConfig(
        search_terms, document_type_terms, dummy=True
    )

    if publisher_terms:
        config.publisher_terms = publisher_terms

    if sort_by:
        config.sort_by = sort_by

    public_gateway_search_results = []
    legislation_search_results = []

    if (
        not config.document_types
        or "standard" in config.document_types
        or "guidance" in config.document_types
    ):
        public_gateway = PublicGateway()
        public_gateway_search_results = public_gateway.search(config)

    # Legislation search
    # If config.search_terms is empty then we don't need to
    # search for legislation
    if (
        "" not in config.search_terms
        and not config.document_types
        or "legislation" in config.document_types
    ):
        legislation = Legislation()
        legislation_search_results = legislation.search(config)

    search_results = []

    for result in public_gateway_search_results:
        search_results.append(
            {
                "id": result["id"],
                "title": result["title"],
                "publisher": result["publisher"],
                "description": result["description"],
                "type": result["type"],
                "date_modified": result["date_modified"],
            }
        )

    for result in legislation_search_results:
        search_results.append(
            {
                "id": result["id"],
                "title": result["title"],
                "publisher": result["publisher"],
                "description": "",
                "type": result["type"],
                "date_modified": result["date_modified"],
            }
        )

    # Convert search_results JSON object to DataFrame
    # (for demonstration purposes)
    search_results_df = pd.DataFrame(search_results)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="search_results.csv"'
    )

    # Write the DataFrame to the response
    writer = csv.writer(response)
    writer.writerow(search_results_df.columns)  # Write the header

    for _, row in search_results_df.iterrows():
        writer.writerow(row)

    return response


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
    form = RegulationSearchForm(request.GET)

    # If the form is not valid, return the form
    if not form.is_valid():
        return render(request, template_name="orp.html", context=context)

    # Add the form to the context
    context["form"] = form

    # Get the search query and document types from the form
    search_query = form.cleaned_data.get("search")
    document_types = form.cleaned_data.get("document_type")

    page = request.GET.get("page", "1")
    # TODO: some page validation is required here
    offset = int(page) if page.isdigit() else 1

    limit = request.GET.get("limit", "10")
    # TODO: some limit validation is required here
    limit = int(limit) if limit.isdigit() else 10

    publisher = request.GET.getlist("publisher", None)
    if publisher:
        logger.info("publisher: %s", publisher)

    # If the search query is empty, return the form
    if not search_query:
        logger.info("no search query provided")
    else:
        logger.info("search query: %s", search_query)

    sort_by = request.GET.get("sort", None)
    if sort_by:
        logger.info("sort by: %s", sort_by)

    logger.info("document types: %s", document_types)
    logger.info("page: %s", offset)

    # Get the search results from the Data API using PublicGateway class
    config = SearchDocumentConfig(
        search_query,
        document_types,
        dummy=True,
        limit=limit,
        offset=offset,
    )

    if publisher:
        config.publisher_terms = publisher

    if sort_by:
        config.sort_by = sort_by

    search_results = []

    if (
        not config.document_types
        or "standard" in config.document_types
        or "guidance" in config.document_types
    ):
        public_gateway = PublicGateway()
        search_results = public_gateway.search(config)

    # Legislation search
    if not config.document_types or "legislation" in config.document_types:
        logger.info("searching for legislation: %s", config.search_terms)
        legislation = Legislation()
        search_results += legislation.search(config)

    # Sort results by date_modified (recent) or relevance
    # (calculate score and sort by score)
    if sort_by == "recent":
        search_results = sorted(
            search_results,
            key=lambda x: parse_date(x["date_modified"]),
            reverse=True,
        )
    elif sort_by == "relevance":
        # Add the 'score' to each search result
        for result in search_results:
            logger.info("result to pass to calculate score: %s", result)
            result["score"] = calculate_score(result, config.search_terms)

        search_results = sorted(
            search_results,
            key=lambda x: x["score"],
            reverse=True,
        )

    context = paginate(context, config, search_results)
    return render(request, template_name="orp.html", context=context)


def search_react(request: HttpRequest) -> HttpResponse:
    """Search view.

    Renders the React based search page.
    """

    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
        "document_types": {
            "standard": "Standard",
            "guidance": "Guidance",
            "legislation": "Legislation",
        },
    }

    return render(request, template_name="react-orp.html", context=context)
