from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.forms import RegulationSearchForm

# from .search import search_data_api


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
    form = RegulationSearchForm(request.GET or None)
    context["form"] = form
    # if form.is_valid() and "query" in request.GET:
    # search_query = form.cleaned_data["query"]
    # search_data = search_data_api(search_query)
    # context["results"] = search_data["results"]
    # context["request_exception"] = search_data["request_exception"]
    # context["truncated"] = search_data["truncated"]
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
