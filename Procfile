release: python manage.py makemigrations && python manage.py migrate
web: gunicorn myapi.wsgi --log-file -