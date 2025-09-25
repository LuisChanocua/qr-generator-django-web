#!/usr/bin/env sh
set -e

# Migraciones al arrancar (usando migrations ya en el repo)
if [ "${MIGRATE_ON_START:-1}" = "1" ]; then
  python manage.py migrate --noinput || true
fi

# Estáticos solo si se indica (prod)
if [ "${DJANGO_COLLECTSTATIC:-0}" = "1" ]; then
  python manage.py collectstatic --noinput
fi

PORT_TO_BIND=${PORT:-8000}

if [ "${DEBUG}" = "true" ]; then
  echo "Starting Django runserver on port ${PORT_TO_BIND} (DEBUG)"
  exec python manage.py runserver 0.0.0.0:${PORT_TO_BIND}
else
  echo "Starting Gunicorn on port ${PORT_TO_BIND}"
  exec gunicorn qrservice.wsgi:application --bind 0.0.0.0:${PORT_TO_BIND} --workers ${WEB_CONCURRENCY:-3}
fi
