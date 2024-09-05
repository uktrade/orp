from django.conf import settings
from django.http import HttpRequest, HttpResponse


def set_analytics_consent_cookie(
    response: HttpResponse, analytics_consent: bool
) -> None:
    """Set analytics consent cookie.

    Sets the analytics consent cookie on the response object.
    """
    response.set_cookie(
        settings.ANALYTICS_CONSENT_NAME,
        value=str(analytics_consent),
        max_age=365 * 24 * 60 * 60,
    )


def get_analytics_consent(request: HttpRequest) -> bool:
    """Get analytics consent.

    Returns the analytics consent boolean value from the request object.
    """
    analytics_consent = request.COOKIES.get(
        settings.ANALYTICS_CONSENT_NAME, None
    )
    return True if analytics_consent == "True" else False


def analytics_form_initial_mapping(analytics_consent: bool) -> dict:
    """Analytics mapping.

    Returns a dictionary with the analytics consent value, which is used to
    initialise the analytics cookie form.
    """
    return {settings.ANALYTICS_CONSENT_NAME: analytics_consent}
