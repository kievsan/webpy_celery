from flask import Flask

from celery_app import celery_app, get_task

app = Flask("app")

app.config['UPLOAD_FOLDER'] = 'files'
celery_app.conf.update(app.config)


####### ЗАКЛИНАНИЕ, чтобы 	CELERY	 работало с	 FLASK:
class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery_app.Task = ContextTask
######	(взято из документации)

