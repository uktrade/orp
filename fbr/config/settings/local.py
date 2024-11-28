"""Local django settings."""

from .base import *  # noqa

# Applications that are required to load before DJANGO_APPS
BASE_APPS = [
    "whitenoise.runserver_nostatic",  # Serve static files via WhiteNoise
    "rest_framework",
]

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#     ]
# }

INSTALLED_APPS = BASE_APPS + INSTALLED_APPS  # noqa
