from celery_app import celery_app
import os

import flask_celery.upscale.upscale as upscale_image
from flask_celery.settings import ML_EXAMPLES, ML_MODEL, ML_STORAGE


@celery_app.task
def upscale_example():
    print('START upscale_example')
    return upscale_image.example(
        os.path.join(ML_EXAMPLES, 'lama_300px.png'),
        os.path.join(ML_STORAGE, 'lama_600px.png'),
        ML_MODEL
    )
