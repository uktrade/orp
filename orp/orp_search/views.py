import base64
import csv
import logging

import pandas as pd

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel
from orp_search.public_gateway import PublicGateway
from orp_search.utils.search import search

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
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
    config = SearchDocumentConfig(search_query="", id=document_id)

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
