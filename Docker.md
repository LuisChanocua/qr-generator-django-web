TL;DR (primer arranque):

# Levantar stack en modo dev (autoreload)
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev up --build

# En otra terminal: crear superusuario
docker compose exec web python manage.py createsuperuser

# Admin: http://localhost:8000/admin/
# QR PNG: http://localhost:8000/q/<slug>.png
# Redirect: http://localhost:8000/r/<slug>

1) Generar el proyecto (solo la primera vez en una máquina nueva)

Si ya existe la carpeta app/, no repitas este paso.

# Build de imagen base
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev build

# Crear proyecto y app dentro del contenedor (se escriben en ./app del host)
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev \
  run --rm --no-deps --entrypoint "" web \
  bash -lc "django-admin startproject qrservice . && python manage.py startapp qrapp && mkdir -p qrapp/migrations && touch qrapp/migrations/__init__.py"


2) Ciclo de desarrollo (comandos típicos)

# Levantar modo dev con override y env-file
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev up --build

# En segundo plano (detached)
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev up -d --build

# Bajar stack
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev down

# Reiniciar solo el servicio web
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev restart web

# Ver estado rápido
docker compose ps

Logs

# Todos los servicios (tail en vivo)
docker compose logs -f

# Solo web / solo db
docker compose logs -f web
docker compose logs -f db

# Últimas N líneas
docker compose logs --tail=100 web


# Ejecutar comandos dentro del contenedor web

# Migraciones
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Crear superusuario
docker compose exec web python manage.py createsuperuser

# Abrir shell de Django
docker compose exec web python manage.py shell

# Colectar estáticos (normalmente solo en prod)
docker compose exec web python manage.py collectstatic --noinput


# Levantar Dev con Logs
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file docker/.env.dev up