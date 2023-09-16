from celery import Celery
from celery.result import AsyncResult

from flask_celery.settings import CELERY_BROKER, CELERY_BACKEND

celery_app = Celery("flask_celery",
                    backend=CELERY_BACKEND,  # os.getenv('CELERY_BACKEND'),
                    broker=CELERY_BROKER)  # os.getenv('CELERY_BROKER')


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)
