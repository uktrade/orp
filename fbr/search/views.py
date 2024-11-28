import csv
import logging

import pandas as pd

from models import DataResponseModel
from utils.search import search, search_database

from django.conf import settings
from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from config import SearchDocumentConfig

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def document(request: HttpRequest, id) -> HttpResponse:
    """
    Document details view.

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
    """
    Handles the download of search results as a CSV file.

    This view function is restricted to the GET HTTP method.
    It accepts several query

    parameters to configure the search:
    - `search`: A string to search within the documents.
    - `document_type`:
        A list of document types to filter the search results.
    - `publisher`: A list of publishers to filter the search results.
    - `sort`: A field name to sort the search results.

    The function constructs a `SearchDocumentConfig` object using the
    received query parameters and performs a search using this
    configuration. `DataResponseModel` objects from the search results
    are retrieved and compiled into a list of dictionaries, which is
    then converted into a DataFrame for demonstration purposes.
    Finally, the ataFrame is written into a CSV file and returned as
    an HTTP response with the appropriate content type and file
    attachment headers.
    """
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
    """
    Search view.

    Renders the Django based search page.
    """
    context = {
        "service_name": settings.SERVICE_NAME_SEARCH,
    }

    context = search(context, request)
    return render(request, template_name="django-fbr.html", context=context)


@require_http_methods(["GET"])
def search_react(request: HttpRequest) -> HttpResponse:
    """
    Search view.

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

    return render(request, template_name="react-fbr.html", context=context)
