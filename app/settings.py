import os

PATH = os.path.join(os.getcwd())

CELERY_BROKER = "redis://db-redis:6379/1"
CELERY_BACKEND = "redis://db-redis:6379/2"

# CELERY_BROKER = os.getenv("CELERY_BROKER")
# CELERY_BACKEND = os.getenv("CELERY_BACKEND")
