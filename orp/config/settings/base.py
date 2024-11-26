"""Django base settings for orp project.

Environment:
We use django-environ but do not read a `.env` file. Locally we provide
docker-compose an environment from `local.env` file in the project root,
using `env_file` field in `docker-compose.yml`. There is a `local.env.example`
in this repo. When deployed, the service retrieves these values from the
environment.

NB: Some settings acquired using `env()` deliberately *do not* have defaults
as we want to get an `ImproperlyConfigured` exception. This highlights badly
configured deployments.
"""

import os

from pathlib import Path
from typing import Any

import dj_database_url
import environ

from django_log_formatter_asim import ASIMFormatter

# Define the root directory (i.e. <repo-root>)
root = environ.Path(__file__) - 4  # i.e. Repository root
SITE_ROOT = Path(root())
# Define the project base directory (i.e. <repo-root>/orp)
BASE_DIR: Path = Path(root(), "orp")

# Get environment variables
env = environ.Env(
    DEBUG=(bool, False),
)

# Must be provided by the environment
SECRET_KEY = env("DJANGO_SECRET_KEY", default="orp-secret-key")

DEBUG = env("DEBUG", default=False)
DJANGO_ADMIN = env("DJANGO_ADMIN", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])
ENVIRONMENT = env(
    "COPILOT_ENVIRONMENT_NAME", default="local"
)  # TODO: Change to APP_ENV, updates required in deploy repo

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "core",
    "orp_search",
]

THIRD_PARTY_APPS: list = [
    "webpack_loader",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.google_tag_manager",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES: dict = {}
if DATABASE_URL := env("DATABASE_URL", default=None):
    DATABASES = {
        "default": {
            **dj_database_url.parse(
                DATABASE_URL,
                engine="postgresql",
            ),
            "ENGINE": "django.db.backends.postgresql",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": SITE_ROOT / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]

# Internationalisation
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_TZ = True

# Static files
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "static/"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Webpack

STATICFILES_DIRS = [
    SITE_ROOT / "front_end/",
]

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "webpack_bundles/",  # must end with slash
        "STATS_FILE": os.path.join(SITE_ROOT, "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "LOADER_CLASS": "webpack_loader.loader.WebpackLoader",
    }
}


# TODO: Use redis for cache?
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Logging
LOGGING: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "asim_formatter": {
            "()": ASIMFormatter,
        },
        "simple": {
            "style": "{",
            "format": "{asctime} {levelname} {message}",
        },
    },
    "handlers": {
        "asim": {
            "class": "logging.StreamHandler",
            "formatter": "asim_formatter",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Django Log Formatter ASIM settings
# See https://github.com/uktrade/django-log-formatter-asim#settings
DLFA_TRACE_HEADERS = ("X-B3-TraceId", "X-B3-SpanId")

# Set the correct handlers when running in DBT Platform
# console handler set as default as it's easier to read
LOGGING["root"]["handlers"] = ["asim"]
LOGGING["loggers"]["django"]["handlers"] = ["asim"]

# ------------------------------------------------------------------------------
# The Open Regulation Platform Zone - specific ORP service settings.
# ------------------------------------------------------------------------------

# Service

SERVICE_NAME: str = "Open Regulation Platform"
SERVICE_NAME_SEARCH: str = "Open Regulation Platform"
CONTACT_EMAIL: str = "paymentpracticesreporting@businessandtrade.gov.uk"

# Cookies
ANALYTICS_CONSENT_NAME: str = "analytics_consent"

# DBT Data API
# DBT_DATA_API_URL = env(
#     "DBT_DATA_API_URL",
#     default="https://data.api.trade.gov.uk/v1/datasets/market-barriers/versions/v1.0.10/data?format=json",  # noqa: E501
# )

# HOSTNAME
HOSTNAME_MAP = {
    "local": "http://localhost:8081",
    "dev": "https://dev.orp.uktrade.digital/",
    "staging": "https://staging.orp.uktrade.digital/",
    "prod": "https://orp.uktrade.digital/",
}

HOSTNAME = HOSTNAME_MAP.get(ENVIRONMENT.lower(), HOSTNAME_MAP["prod"])

# Google Analytics (GA)
# Note: please consult the performance team before changing these settings
COOKIE_PREFERENCES_SET_NAME: str = "cookie_preferences_set"
COOKIE_ACCEPTED_GA_NAME: str = "accepted_ga_cookies"
GOOGLE_ANALYTICS_TAG_MANAGER_ID = env(
    "GOOGLE_ANALYTICS_TAG_MANAGER_ID", default=None
)
