#!/bin/sh
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DJANGO_SUPER_USER}', '${DJANGO_EMAIL}', '${DJANGO_PASS}')" | python manage.py shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000