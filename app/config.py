import os

CELERY_BROKER = os.getenv("CELERY_BROKER")
CELERY_BACKEND = os.getenv("CELERY_BACKEND")

