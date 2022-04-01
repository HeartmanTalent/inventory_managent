#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

./manage.py flush --no-input
./manage.py makemigrations
./manage.py migrate
# ./manage.py loaddata initial_data
./manage.py collectstatic --no-input --clear
# gunicorn easylocum.wsgi:application --bind 0.0.0.0:8000 --workers 3
./manage.py runserver 0.0.0.0:8001