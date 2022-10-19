web: python fedemy_shipments/manage.py runserver 0.0.0.0:$PORT

release: python fedemy_shipments/manage.py makemigrations --noinput
release: python fedemy_shipments/manage.py collectstatic --noinput
release: python fedemy_shipments/manage.py migrate --noinput