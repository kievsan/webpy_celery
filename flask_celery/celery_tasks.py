import time

from flask_celery.celery_app import celery_app1
import flask_celery.upscale.upscale as upscale_image

upscale_image_task = celery_app1.task(upscale_image.upscale_on_server)
upscale_example_task = celery_app1.task(upscale_image.upscale_example)


@celery_app1.task
def simple_task(msg: str):
    print('START SIMPLE example')
    words = msg.split()
    words.reverse()
    time.sleep(5)
    return ' '.join(words)
