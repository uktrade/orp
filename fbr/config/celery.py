from celery import Celery

app = Celery("fbr_celery")

# Load settings from Django or directly
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in installed apps
app.autodiscover_tasks()
