import time

import flask_celery.upscale.upscale as upscale_image
from flask_celery.celery_stuff.app import celery_app


upscale_image_task = celery_app.task(
    upscale_image.upscale_on_server,
    name='flask_celery.celery_stuff.tasks.upscale_image'
)

upscale_example_task = celery_app.task(
    upscale_image.upscale_example,
    name='flask_celery.celery_stuff.tasks.upscale_example'
)


@celery_app.task(name='flask_celery.celery_stuff.tasks.simple')
def simple_task(msg: str):
    print('START SIMPLE example')
    words = msg.split()
    words.reverse()
    time.sleep(5)
    return ' '.join(words)
