import os
from flask_celery.celery_app import celery_app
from flask_celery.settings import ML_EXAMPLES, ML_STORAGE
import flask_celery.upscale.upscale as upscale_image


upscale_image_task = celery_app.task(upscale_image.upscale_on_server)

@celery_app.task
def upscale_image_example():
    print('START upscale_example')
    return upscale_image.local_example(
        os.path.join(ML_EXAMPLES, 'lama_300px.png'),
        os.path.join(ML_STORAGE, 'lama_600px.png'))
