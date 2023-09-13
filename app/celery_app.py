from celery import Celery
from celery.result import AsyncResult

from conf import CELERY_BROKER, CELERY_BACKEND


celery_app1 = Celery(main="app",
                    backend=CELERY_BACKEND,
                    broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app1)


@celery_app1.task
def celery_task():
    return 0
