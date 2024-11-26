from django.conf import settings
from django.http import HttpRequest, HttpResponse


def set_ga_cookie_policy(response: HttpResponse, preference: str) -> None:
    """Set Google Analytics (GA) policy.

    Sets the cookies that are required for Google Tag Manager (GTM) to
    function correctly.
    """
    response.set_cookie(
        key=settings.COOKIE_ACCEPTED_GA_NAME,
        value=preference,
        max_age=365 * 24 * 60 * 60,
    )
    response.set_cookie(
        key=settings.COOKIE_PREFERENCES_SET_NAME,
        value="true",
        max_age=365 * 24 * 60 * 60,
    )


def get_ga_cookie_preference(request: HttpRequest) -> str:
    """Get Google Analytics (GA) cookie preference.

    Returns value of the GA cookie preference if it exists, otherwise
    returns "false".
    """
    return request.COOKIES.get(settings.COOKIE_ACCEPTED_GA_NAME, "false")
