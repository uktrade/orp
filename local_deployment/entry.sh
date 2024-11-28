#!/bin/sh -e

echo "Installing node modules"
npm install

echo "Bundling WebPack"
npm run build

. "$(poetry env info --path)/bin/activate"

echo "Collecting Static Files"
python fbr/manage.py collectstatic --noinput

# echo "Check missing migrations"
# python prompt_payments/manage.py makemigrations --check --dry-run

echo "Starting server"
python fbr/manage.py runserver 0.0.0.0:8080
