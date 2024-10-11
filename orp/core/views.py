from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_safe

from .cookies import (
    analytics_form_initial_mapping,
    get_analytics_consent,
    set_analytics_consent_cookie,
)
from .forms import CookiePageConsentForm
from .healthcheck import application_service_health


@require_http_methods(["GET"])
def home(request: HttpRequest) -> HttpResponse:
    """Home.

    If we're in prod, redirect to the GOV.UK page, otherwise render a dev home
    page.
    """
    if request.META.get("HTTP_HOST") == "orp.uktrade.digital":
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
    """Cookies.

    Returns the cookies page. If the request method is POST, the analytics
    consent cookie is set and the user is redirected back to the cookies page.
    """
    context = {
        "service_name": settings.SERVICE_NAME,
        "analytics_cookie_name": settings.ANALYTICS_CONSENT_NAME,
    }
    if request.method == "POST":
        form = CookiePageConsentForm(request.POST)
        if form.is_valid():
            analytics_consent = form.cleaned_data[
                settings.ANALYTICS_CONSENT_NAME
            ]
            context[settings.ANALYTICS_CONSENT_NAME] = analytics_consent
            response = redirect(reverse("cookies"))
            set_analytics_consent_cookie(response, analytics_consent)
            response[
                "Location"
            ] += f"?{settings.ANALYTICS_CONSENT_NAME}={analytics_consent}"
            return response
    else:
        analytics_consent = get_analytics_consent(request)
        form = CookiePageConsentForm(
            initial=analytics_form_initial_mapping(analytics_consent)
        )
    context["form"] = form
    return render(request, template_name="cookies.html", context=context)


@require_http_methods(["GET"])
def set_cookie_banner_preference(request) -> HttpResponseRedirect:
    """Set cookie banner preference.

    Sets analytics cookie preference and redirects to the current page.
    The redirect URL includes the `cookie_preferences` query parameter.
    This parameter is used to display a confirmation message banner.
    """
    analytics_consent = request.GET.get(settings.ANALYTICS_CONSENT_NAME)
    current_page = request.GET.get("current_page") or "/"
    separator = "?" if "?" not in current_page else "#"
    current_page = (
        f"{current_page}{separator}cookie_preferences={analytics_consent}"
    )
    response = redirect(current_page)
    set_analytics_consent_cookie(response, analytics_consent)
    return response


@require_http_methods(["GET"])
def hide_cookie_banner(request) -> HttpResponseRedirect:
    """Hide the cookie banner.

    Redirects to the current page without any query parameters,
    effectively hiding the cookie banner.
    """
    current_page = request.GET.get("current_page") or "/"
    return redirect(current_page)
