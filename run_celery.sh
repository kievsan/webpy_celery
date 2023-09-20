celery -A flask_celery.celery_stuff.app.celery_app -b "redis://127.0.0.1:6380/1" --result-backend "redis://127.0.0.1:6380/2" worker -c 2 -l info
