import os

CELERY_BROKER = "redis://db-redis:6379/1"
CELERY_BACKEND = "redis://db-redis:6379/2"

CURRENT_PATH = os.path.join(os.getcwd())
# ML_PATH = os.path.join(os.getcwd(), "upscale")
ML_PATH = CURRENT_PATH
ML_OBJECTS = os.path.join(ML_PATH, "examples")
ML_STORAGE = os.path.join(ML_PATH, "storage")
ML_MODEL = os.path.join(ML_PATH, "models", "EDSR_x2.pb")

# CELERY_BROKER = os.getenv("CELERY_BROKER")
# CELERY_BACKEND = os.getenv("CELERY_BACKEND")
# CELERY_STORAGE = os.getenv("ML_STORAGE")

# ML_PATH = os.path.join(os.getcwd(), os.getenv("ML_PACKAGE"))
# ML_OBJECTS = os.path.join(ML_PATH, os.getenv("ML_OBJECTS_FOLDER"))
# ML_STORAGE = os.path.join(ML_PATH, os.getenv("ML_STORAGE"))
# ML_MODEL = os.path.join(ML_PATH,
#                         os.getenv("ML_MODELS_FOLDER"),
#                         os.getenv("ML_CURRENT_MODEL_NAME"))
