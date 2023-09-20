from celery import Celery
from celery.result import AsyncResult

from flask_celery.settings import CELERY_BROKER, CELERY_BACKEND

celery_app = Celery("celery_app",
                    backend="redis://127.0.0.1:6380/2",
                    broker="redis://127.0.0.1:6380/1",
                    include=['flask_celery.celery_stuff.tasks'])
                    # backend=CELERY_BACKEND,  # os.getenv('CELERY_BACKEND'),
                    # broker=CELERY_BROKER)  # os.getenv('CELERY_BROKER'))


def get_task_result(task_id: str) -> AsyncResult:
    print('start def celery_app.get_task')  #############
    return AsyncResult(task_id, app=celery_app)
