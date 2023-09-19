import base64
import os
import uuid

from flask import jsonify, request, send_file
from flask.views import MethodView
import redis

from flask_celery.celery_app import get_task
import flask_celery.celery_tasks as celery
import flask_celery.settings as conf
# from flask_celery.celery_tasks import upscale_image_task, upscale_example_task
# from flask_celery.settings import REDIS_HOST, CELERY_STORAGE, ML_PACKAGE, ML_EXAMPLES


# redis storage

redis_dict = redis.Redis(host='127.0.0.1', port=6380)
# redis_dict = redis.Redis(host=conf.REDIS_HOST)


# views

def main_view():
    return jsonify({'message': 'Hi!'})


class SimpleView(MethodView):
    def post(self):
        print('start def SimpleView.post') #############
        msg = request.json.get('message')
        task = celery.simple_task.delay(msg)
        redis_dict.mset({task.id: msg})
        return jsonify({'task_id': task.id})

    def get(self, task_id):
        print('start def SimpleView.get') #############
        task = get_task(task_id)
        status = task.status
        data = {'status': status}
        if status == 'SUCCESS':
            phrase = redis_dict.get(task_id)
            data.update({'pun': task.result})
        return jsonify(data)


class ExampleView(MethodView):
    def post(self):
        print('start def ExampleView.post') #############
        input_path, upscale_path = self.get_path('filename')
        print(input_path, '\n', upscale_path) ####
        task = celery.upscale_example_task.delay(input_path, upscale_path)
        redis_dict.mset({task.id: upscale_path})
        return jsonify({'task_id': task.id})

    def get_path(self, field):
        print('start def ExampleView.get_path') #############
        filename = request.json.get(field)
        extension = '.'
        extension += filename.split(extension)[-1]
        name = filename[:filename.rfind(extension)]
        unic = uuid.uuid4()
        upscale_filename = f'upscale_{name}_{unic}{extension}'
        upscale_path = os.path.join(conf.PATH,
                                    conf.ML_PACKAGE, conf.ML_STORAGE,
                                    upscale_filename)
        input_path = os.path.join(conf.PATH,
                                  conf.ML_PACKAGE, conf.ML_EXAMPLES,
                                  filename)
        return input_path, upscale_path


class TaskView(MethodView):
    def get(self, task_id):
        print('start def TaskView.get') #############
        task = get_task(task_id)
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
        upscale_image = os.path.join(conf.CELERY_STORAGE, upscale_filename)
        # image.filename = upscale_filename
        img = base64.b64encode(image.read())
        image_str = img.decode()
        # image_str = image.read().decode()
        # task = upscale_example_task.delay(image_str, upscale_image)
        task = celery.upscale_image_task.delay(image_str, upscale_image)
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
        return send_file(os.path.join(conf.CELERY_STORAGE, file), mimetype='image/gif')




