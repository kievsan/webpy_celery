from dotenv import load_dotenv
import os

load_dotenv()


PATH = os.path.join(os.getcwd())

CELERY_BROKER = os.getenv("CELERY_BROKER")
CELERY_BACKEND = os.getenv("CELERY_BACKEND")

ML_PACKAGE = os.getenv("ML_PACKAGE")
ML_STORAGE = os.getenv("ML_STORAGE")
ML_EXAMPLES = os.getenv("ML_OBJECTS_FOLDER")
ML_MODELS_FOLDER = os.getenv("ML_MODELS_FOLDER")
ML_MODEL_NAME = os.getenv("ML_CURRENT_MODEL_NAME")
ML_MODEL = os.path.join(ML_MODELS_FOLDER, ML_MODEL_NAME)
