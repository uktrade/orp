web: bash paas_entrypoint.sh
celery-worker: celery --app fbr.config.celery worker --task-events --loglevel INFO
celery-beat: celery --app fbr.config.celery beat --loglevel INFO
