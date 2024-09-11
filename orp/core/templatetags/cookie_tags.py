from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def render_cookie_banner(context) -> str:
    """Renders the cookie banner.

    Renders the cookie banner if the analytics cookie is not set.
    If the `cookie_preferences` query parameter is present, then
    the confirmation banner is rendered. Otherwise, the cookie banner
    is not rendered.
    """
    request = context["request"]
    if settings.ANALYTICS_CONSENT_NAME not in request.COOKIES:
        return render_to_string(
            "cookie_banner.html",
            {
                "service_name": settings.SERVICE_NAME,
                "analytics_cookie_name": settings.ANALYTICS_CONSENT_NAME,
                "request": request,
                "show_cookie_banner": True,
                "show_confirmation_message": False,
            },
        )
    elif "cookie_preferences" in request.GET:
        return render_to_string(
            "cookie_banner.html",
            {
                "service_name": settings.SERVICE_NAME,
                "cookie_preferences": request.GET.get("cookie_preferences"),
                "request": request,
                "show_cookie_banner": False,
                "show_confirmation_message": True,
            },
        )
    return ""
