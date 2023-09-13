import time

from celery import Celery
from celery.result import AsyncResult

from conf import CELERY_BROKER, CELERY_BACKEND

celery_app = Celery(main="app",
                     backend=CELERY_BACKEND,
                     broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)


@celery_app.task
def celery_task():
    print('START')
    time.sleep(1)
    return 0
