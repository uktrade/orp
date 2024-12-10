#!/bin/sh -e

echo "Installing node modules"
npm install

echo "Bundling WebPack"
npm run build

echo "Collecting Static Files"
python manage.py collectstatic --noinput

echo "Starting server"
python manage.py runserver 0.0.0.0:8080
