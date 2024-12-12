#!/bin/bash

set -ex # Prints each command as it runs. If a command fails, it will halt at that point

poetry run python manage.py migrate --noinput

# Start the server
poetry run gunicorn fbr.wsgi:application --bind "0.0.0.0:$PORT"
