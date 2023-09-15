PYTHONUNBUFFERED=TRUE gunicorn -b 0.0.0.0:5000 --capture-output flask_celery.app:flask_app
#PYTHONUNBUFFERED=TRUE gunicorn -b 0.0.0.0:5000 app:app --capture-output
