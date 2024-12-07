from __future__ import absolute_import, unicode_literals

# This ensures the app is always imported when Django starts
# allowing shared_task to utilize this app.
from .config.celery import celery_app

__all__ = ("celery_app",)
