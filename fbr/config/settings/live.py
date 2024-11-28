import os

import dj_database_url
import sentry_sdk

from dbt_copilot_python.database import database_url_from_env
from dbt_copilot_python.network import setup_allowed_hosts
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa

ALLOWED_HOSTS = setup_allowed_hosts(ALLOWED_HOSTS)  # noqa

DATABASES["default"] = dj_database_url.config(  # noqa
    default=database_url_from_env("DATABASE_CREDENTIALS")
)

sentry_sdk.init(
    os.environ.get("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
)
