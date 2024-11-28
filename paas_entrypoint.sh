#!/bin/bash

set -ex # Prints each command as it runs. If a command fails, it will halt at that point

cd fbr || exit 1
poetry run python manage.py migrate --noinput
poetry run gunicorn config.wsgi --bind "0.0.0.0:$PORT"
