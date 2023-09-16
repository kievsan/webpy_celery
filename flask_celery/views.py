import base64
import os
import uuid

from celery.result import AsyncResult
from flask import jsonify, request, send_file
from flask.views import MethodView
import redis

from flask_celery.celery_app import celery_app, get_task
from flask_celery.celery_tasks import upscale_image_task
from flask_celery.settings import REDIS_HOST, CELERY_STORAGE


# redis storage

redis_dict = redis.Redis(host=REDIS_HOST)


# views

def main_view():
    return jsonify({'message': 'Hi!'})


class TaskView(MethodView):
    def get(self, task_id):
        task = AsyncResult(task_id, app=celery_app)
        status = task.status
        message = {'status': status}
        if status == 'SUCCESS':
            file_name = redis_dict.get(task_id)
            message.update({'link': f'{request.url_root}processed/{file_name.decode()}'})
        return jsonify(message)

    def post(self):
        image = request.files.get('image')
        name = image.filename[:image.filename.rfind('.')]
        extension = image.filename[image.filename.rfind('.'):]
        unic = uuid.uuid4()
        upscale_filename = f'upscale_{name}_{unic}{extension}'
        upscale_image = os.path.join(CELERY_STORAGE, upscale_filename)
        image.filename = upscale_filename
        image_str = image.read().decode()
        task = upscale_image_task.delay(image_str)
        redis_dict.mset({task.id: upscale_image})
        return jsonify({'task_id': task.id})

    def _get_image(self):
        image = request.files.get('image')
        filename = image.filename
        extension = filename[filename.rfind('.'):]
        file_name = uuid.uuid4()
        image.filename = f'{file_name}{extension}'
        return image


class ImageView(MethodView):
    def get(self, file):
        return send_file(os.path.join(CELERY_STORAGE, file), mimetype='image/gif')





