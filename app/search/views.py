import logging

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from app.search.config import SearchDocumentConfig
from app.search.utils.search import search, search_database

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
        context["result"] = queryset
    except Exception as e:
        logger.error("error fetching details: %s", e)
        context["error"] = f"error fetching details: {e}"

    return render(request, template_name="document.html", context=context)


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
