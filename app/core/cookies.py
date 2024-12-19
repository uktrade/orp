import json
import logging

from django.conf import settings
from django.http import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)


def set_ga_cookie_policy(response: HttpResponse, preference: str) -> None:
    """Set Google Analytics (GA) policy.

    Sets the cookies that are required for Google Tag Manager (GTM) to
    function correctly.
    """

    cookie_object = {
        "essential": True,
        "settings": True,
        "usage": preference == "true",
        "campaigns": False,
    }

    json_string_cookie_object = json.dumps(cookie_object)

    response.set_cookie(
        key=settings.COOKIE_ACCEPTED_GA_NAME,
        value=json_string_cookie_object,
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
    cookie_object = request.COOKIES.get(settings.COOKIE_ACCEPTED_GA_NAME)
    if cookie_object:
        try:
            cookie_value = json.loads(cookie_object)
            return str(cookie_value.get("usage", False)).lower()
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing GA cookie: {e}")

    return "false"
