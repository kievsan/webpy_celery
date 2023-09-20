from dotenv import load_dotenv
import os

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

load_dotenv()

PATH = os.path.join(os.getcwd())

APP_PACKAGE= os.getenv("APP_PACKAGE")

ML_PACKAGE = os.getenv("ML_PACKAGE")
ML_STORAGE = os.getenv("ML_STORAGE")
ML_EXAMPLES = os.getenv("ML_OBJECTS_FOLDER")
ML_MODELS_FOLDER = os.getenv("ML_MODELS_FOLDER")
ML_MODEL_NAME = os.getenv("ML_CURRENT_MODEL_NAME")
ML_MODEL = os.path.join(ML_MODELS_FOLDER, ML_MODEL_NAME)

PG_ENGINE = os.getenv('PG_ENGINE')
PG_NAME = os.getenv('PG_NAME')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_HOST_PORT')
PG_DSN = f'{PG_ENGINE}://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'

REDIS_ENGINE = os.getenv('REDIS_ENGINE')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_HOST_PORT = os.getenv('REDIS_HOST_PORT')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_BROKER_DB = os.getenv('REDIS_BROKER_DB')
REDIS_BACKEND_DB = os.getenv('REDIS_BACKEND_DB')
REDIS_DSN = f'{REDIS_ENGINE}://{REDIS_HOST}:{REDIS_PORT}'

CELERY_BROKER = f'{REDIS_DSN}/{REDIS_BROKER_DB}'
CELERY_BACKEND = f'{REDIS_DSN}/{REDIS_BACKEND_DB}'
# CELERY_BACKEND = f"db+{PG_DSN}"
CELERY_STORAGE = os.path.join(ML_PACKAGE, ML_STORAGE)

STORAGE = os.path.join(PATH, APP_PACKAGE, ML_PACKAGE, ML_STORAGE)
