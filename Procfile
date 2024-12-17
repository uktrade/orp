web: bash paas_entrypoint.sh
celery-worker: celery --app fbr.celery_app worker --task-events --loglevel INFO
celery-beat: celery --app fbr.celery_app beat --loglevel INFO
check: python manage.py check
