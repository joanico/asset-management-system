#!/bin/bash

set -e

# Wait for PostgreSQL if we're using it
if [ "$DATABASE_ENGINE" = "django.db.backends.postgresql" ]; then
  echo "Waiting for PostgreSQL..."
  while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started"
fi

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Collect static files if in production
if [ "$DJANGO_SETTINGS_MODULE" = "mini_project.settings.production" ]; then
  echo "Collect static files"
  python manage.py collectstatic --noinput
fi

# Create superuser if needed
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL \
    || true
fi

# Start server
if [ "$1" = "runserver" ]; then
  exec python manage.py runserver 0.0.0.0:8000
elif [ "$1" = "gunicorn" ]; then
  exec gunicorn mini_project.wsgi:application --bind 0.0.0.0:8000
else
  exec "$@"
fi 