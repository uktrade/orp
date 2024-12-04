import os

from celery import Celery
from celery.schedules import crontab
from dbt_copilot_python.celery_health_check import healthcheck

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

celery_app = Celery("fbr_celery")
celery_app.config_from_object(
    "django.conf:config.settings.local", namespace="CELERY"
)
celery_app.autodiscover_tasks()

celery_app = healthcheck.setup(celery_app)

celery_app.conf.beat_schedule = {
    "schedule-fbr-cache-task": {
        "task": "cache.tasks.rebuild_cache",
        "schedule": crontab(hour="1", minute="0"),
    },
}
