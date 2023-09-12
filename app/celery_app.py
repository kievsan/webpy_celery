
from celery import Celery
from celery.result import AsyncResult

from config import CELERY_BROKER, CELERY_BACKEND


celery_app = Celery("app", backend=CELERY_BACKEND, broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)


@celery_app.task
def celery_task():
    return 0
