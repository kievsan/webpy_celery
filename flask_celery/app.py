from flask import Flask

from flask_celery.celery_app import celery_app, get_task
import flask_celery.settings as conf

flask_app = Flask("flask_celery")

celery_app.conf.update(flask_app.config)


####### ЗАКЛИНАНИЕ, чтобы 	CELERY	 работало с	 FLASK:
class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery_app.Task = ContextTask
######	(взято из документации)


if __name__ == '__main__':
    flask_app.run()

