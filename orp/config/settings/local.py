"""Local django settings."""

from .base import *  # noqa

# Applications that are required to load before DJANGO_APPS
BASE_APPS = [
    "whitenoise.runserver_nostatic",  # Serve static files via WhiteNoise
]

INSTALLED_APPS = BASE_APPS + INSTALLED_APPS  # noqa
