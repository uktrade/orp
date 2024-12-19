from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def render_service_problem(context) -> str:
    """Render the service problem page for dynamic errors.

    This tag is used to display a service problem page when there's an issue
    with a third-party service, while our site remains functional.
    """
    return render_to_string(
        "service_problem.html",
        context={"contact_email": settings.CONTACT_EMAIL},
    )
