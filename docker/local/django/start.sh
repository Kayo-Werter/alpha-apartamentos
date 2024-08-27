#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

chown -R django:django /app
chmod -R 755 /app

python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec python manage.py runserver 0.0.0.0:8000