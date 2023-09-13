import os

CELERY_BROKER = os.getenv("CELERY_BROKER")
CELERY_BACKEND = os.getenv("CELERY_BACKEND")

CURRENT_PATH = os.getcwd()

ML_PATH = os.path.join(CURRENT_PATH, os.getenv("ML_PACKAGE"))
ML_OBJECTS = os.path.join(ML_PATH, os.getenv("ML_OBJECTS_FOLDER"))
ML_RESULTS = os.path.join(ML_PATH, os.getenv("ML_RESULTS_FOLDER"))
ML_MODEL = os.path.join(ML_PATH,
                        os.getenv("ML_MODELS_FOLDER"),
                        os.getenv("ML_CURRENT_MODEL_NAME"))
