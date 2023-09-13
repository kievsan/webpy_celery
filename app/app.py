from flask import Flask

from conf import ML_RESULTS
from celery_app import celery_app1, get_task

flask_app = Flask("app")

flask_app.config['UPLOAD_FOLDER'] = ML_RESULTS
celery_app1.conf.update(flask_app.config)


####### ЗАКЛИНАНИЕ, чтобы 	CELERY	 работало с	 FLASK:
class ContextTask(celery_app1.Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery_app1.Task = ContextTask
######	(взято из документации)

