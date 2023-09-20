from flask import Flask

from flask_celery.celery_stuff.app import celery_app
import flask_celery.views as views

flask_app = Flask("flask_celery")
flask_app.config['UPLOAD_FOLDER'] = 'files'

celery_app.conf.update(flask_app.config)

####### чтобы 	CELERY	 работало с	 FLASK:
class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery_app.Task = ContextTask
######	(взято из документации)


# rules

flask_app.add_url_rule('/',
                 view_func=views.main_view,
                 methods=['GET'])

flask_app.add_url_rule('/simple/',
                 view_func=views.SimpleView.as_view('simple_add'),
                 methods=['POST'])

flask_app.add_url_rule('/simple/<task_id>',
                 view_func=views.SimpleView.as_view('simple_get'),
                 methods=['GET'])

flask_app.add_url_rule('/example/',
                 view_func=views.ExampleView.as_view('example_add'),
                 methods=['POST'])

flask_app.add_url_rule('/upscale/',
                 view_func=views.TaskView.as_view('task_add'),
                 methods=['POST'])

flask_app.add_url_rule('/tasks/<task_id>',
                 view_func=views.TaskView.as_view('task_get'),
                 methods=['GET'])

flask_app.add_url_rule('/processed/<file>',
                 view_func=views.ImageView.as_view('image_get'),
                 methods=['GET'])


if __name__ == '__main__':
    flask_app.run('127.0.0.1', port=5000)

