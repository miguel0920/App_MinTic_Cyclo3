web: gunicorn fedemyShipments.wsgi --log-file -

release: python manage.py makemigrations --noinput
release: python manage.py collectstatic -i rest_framework
release: python manage.py migrate --noinput