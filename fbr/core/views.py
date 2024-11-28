from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods, require_safe

from .cookies import get_ga_cookie_preference, set_ga_cookie_policy
from .forms import CookiePreferenceForm
from .healthcheck import application_service_health


@require_http_methods(["GET"])
def home(request: HttpRequest) -> HttpResponse:
    """Home.

    If we're in prod, redirect to the GOV.UK page, otherwise render a dev home
    page.
    """
    if (
        request.META.get("HTTP_HOST")
        == "find-business-regulations.uktrade.digital"
    ):
        return HttpResponse(
            content="Redirecting to GOV.UK",
            status=302,
            headers={"Location": "https://www.gov.uk"},
        )
    context = {
        "service_name": f"{settings.SERVICE_NAME} - Development",
    }
    return render(request, template_name="home.html", context=context)


@require_safe
def health_check(request: HttpRequest) -> HttpResponse:
    """Healthcheck endpoint.

    Returns HttpResponse: If status contains `OK`, the response has a status
    code of 200, otherwise the response status is set to 503. Cache control
    headers are set appropriately.
    """
    status = application_service_health()

    if "ok" in status.lower():
        response = HttpResponse(status, content_type="text/xml", status=200)
    else:
        response = HttpResponse(status, content_type="text/xml", status=503)
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@require_http_methods(["GET"])
def privacy_notice(request: HttpRequest) -> HttpResponse:
    """Privacy.

    Returns privacy policy page.
    """
    context = {
        "service_name": settings.SERVICE_NAME,
    }
    return render(
        request, template_name="privacy_notice.html", context=context
    )


@require_http_methods(["GET"])
def accessibility_statement(request: HttpRequest) -> HttpResponse:
    """Accessibility statement.

    Returns the accessibility statement page.
    """
    context = {
        "service_name": settings.SERVICE_NAME,
        "contact_email": settings.CONTACT_EMAIL,
    }
    return render(
        request, template_name="accessibility_statement.html", context=context
    )


@require_http_methods(["GET", "POST"])
def cookies(request: HttpRequest) -> HttpResponse:
    """Cookie policy page view.

    Returns the cookies page. If the request method is POST, the analytics
    consent cookie is set and the user is redirected back to the cookies page.
    """
    context = {
        "service_name": settings.SERVICE_NAME,
        "cookie_preference_name": settings.COOKIE_ACCEPTED_GA_NAME,
    }
    if request.method == "POST":
        form = CookiePreferenceForm(request.POST)
        if form.is_valid():
            preference = form.cleaned_data["cookie_preference"]
            response = redirect(reverse("cookies"))
            set_ga_cookie_policy(response, preference)
            response[
                "Location"
            ] += f"?{settings.COOKIE_ACCEPTED_GA_NAME}={preference}"
            return response
    else:
        preferences_value = get_ga_cookie_preference(request)
        form = CookiePreferenceForm(
            initial={"cookie_preference": preferences_value}
        )
    context["form"] = form
    return render(request, template_name="cookies.html", context=context)


@require_http_methods(["GET"])
def set_cookie_banner_preference(request) -> HttpResponseRedirect:
    """Set cookie preferences banner.

    Sets the user Google Analytics (GA) cookie preference and then redirects
    to the current page. The redirect URL includes the `hide_banner`
    query parameter. This parameter is used to display a confirmation message
    banner.
    """
    preference = request.GET.get(settings.COOKIE_ACCEPTED_GA_NAME, "false")
    current_page = request.GET.get("current_page")
    if not url_has_allowed_host_and_scheme(
        url=current_page,
        allowed_hosts={request.get_host()}.union(settings.ALLOWED_HOSTS),
        require_https=request.is_secure(),
    ):
        current_page = "/"
    separator = "?" if "?" not in current_page else "&"
    current_page = (
        f"{current_page}{separator}hide_banner=true"
        f"&{settings.COOKIE_ACCEPTED_GA_NAME}={preference}"
    )
    response = redirect(current_page)
    set_ga_cookie_policy(response, preference)
    return response


@require_http_methods(["GET"])
def hide_cookie_banner(request) -> HttpResponseRedirect:
    """Hide the cookie banner.

    Redirects to the current page without any query parameters,
    effectively hiding the cookie banner.
    """
    current_page = request.GET.get("current_page")
    if not url_has_allowed_host_and_scheme(
        url=current_page,
        allowed_hosts={request.get_host()}.union(settings.ALLOWED_HOSTS),
        require_https=request.is_secure(),
    ):
        current_page = "/"
    return redirect(current_page)