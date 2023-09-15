from celery_app import celery_app
from upscale import upscale as upscale_image


@celery_app.task
def upscale_example():
    print('START upscale_example')
    return upscale_image.example('examples/lama_300px.png',
                                 'examples/lama_600px.png',
                                 'models/EDSR_x2.pb')
