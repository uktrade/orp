#!/bin/sh -e

echo "Installing node modules"
npm install

echo "Bundling WebPack"
npm run build

. "$(poetry env info --path)/bin/activate"

echo "Collecting Static Files"
python orp/manage.py collectstatic --noinput

echo "Starting server"
python orp/manage.py runserver 0.0.0.0:8080
