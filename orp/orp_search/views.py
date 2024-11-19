import csv
import logging

import pandas as pd

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel
from orp_search.utils.search import search, search_database

from django.conf import settings
from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def document(request: HttpRequest, id) -> HttpResponse:
    """Document details view.

    Handles the GET request to fetch details based on the provided id.
    """
    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    if not id:
        context["error"] = "id parameter is required"
        return render(request, template_name="document.html", context=context)

    # Create a search configuration object with the provided id
    config = SearchDocumentConfig(search_query="", id=id)

    try:
        queryset = search_database(config)
        context["result"] = serialize("json", queryset)
    except Exception as e:
        logger.error("error fetching details: %s", e)
        context["error"] = f"error fetching details: {e}"

    return render(request, template_name="document.html", context=context)


@require_http_methods(["GET"])
def download_search_csv(request: HttpRequest) -> HttpResponse:
    search_query = request.GET.get("search", "")
    document_types = request.GET.getlist("document_type", "")
    publishers = request.GET.getlist("publisher", None)
    sort_by = request.GET.get("sort", None)
    config = SearchDocumentConfig(
        search_query,
        document_types,
        publisher_names=publishers,
        sort_by=sort_by,
    )
    # Perform search
    search(config)

    # Get DataResponseModel objects from the search results
    documents = DataResponseModel.objects.all()

    search_results = []
    for result in documents:
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
def search_django(request: HttpRequest):
    """Search view.

    Renders the Django based search page.
    """
    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    context = search(context, request)
    return render(request, template_name="orp.html", context=context)


@require_http_methods(["GET"])
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
