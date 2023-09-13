from celery import Celery
from celery.result import AsyncResult

from upscale import upscale as upscale_image
from settings import CELERY_BROKER, CELERY_BACKEND

celery_app = Celery(main="app",
                     backend=CELERY_BACKEND,
                     broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)


@celery_app.task
def upscale_example():
    print('START upscale_example')
    return upscale_image.example('examples/lama_300px.png',
                                 'examples/lama_600px.png',
                                 'models/EDSR_x2.pb')
