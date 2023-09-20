from celery import Celery
from celery.result import AsyncResult

celery_app = Celery("flask_celery.celery_stuff.app",
                    backend="redis://127.0.0.1:6380/2",
                    broker="redis://127.0.0.1:6380/1",
                    include=['flask_celery.celery_stuff.tasks']
                    )
# celery_app.autodiscover_tasks('tasks')


def get_task_result(task_id: str) -> AsyncResult:
    print('start def celery_app.get_task')  #############
    return AsyncResult(task_id, app=celery_app)
