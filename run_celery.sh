celery -A flask_celery.celery_app.celery_app1 -b "redis://127.0.0.1:6380/1" --result-backend "redis://127.0.0.1:6380/2" worker -c 2 -l info
