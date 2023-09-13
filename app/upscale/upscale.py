import cv2
from cv2 import dnn_superres

from functools import lru_cache
import datetime

# import os

# ML_OBJECTS = os.path.join(ML_PATH, os.getenv("ML_OBJECTS_FOLDER"))
# ML_STORAGE = os.path.join(ML_PATH, os.getenv("ML_STORAGE"))
# ML_MODEL = os.path.join(ML_PATH,
#                         os.getenv("ML_MODELS_FOLDER"),
#                         os.getenv("ML_CURRENT_MODEL_NAME"))

# ml_path = os.path.join(os.getcwd())
# ml_objects = os.path.join(ml_path, "examples")
# ml_storage = os.path.join(ml_path, "storage")
# ml_model = os.path.join(ml_path, "models", "EDSR_x2.pb")


@lru_cache
def scaler(model_path: str):
    """
    :param model_path: путь к ИИ модели
    :return:
    """
    scaler = dnn_superres.DnnSuperResImpl.create()
    scaler.readModel(model_path)
    scaler.setModel('edsr', 2)
    return scaler


def upscale(input_path: str, output_path: str, model_path: str) -> str:
    """
        :param input_path: путь к изображению для апскейла
        :param output_path:  путь к выходному файлу
        :param model_path: путь к ИИ модели
        :return:
    """
    print('Starting to make upscale image for', input_path)

    try:
        print('reading...')
        image = cv2.imread(input_path)
    except FileNotFoundError as err:
        print(err)
        return ''

    print('upscaling...')
    result = scaler(model_path).upsample(image)

    try:
        print('writing...')
        cv2.imwrite(output_path, result)
    except OSError as err:
        print(err)
        return ''

    return output_path


def example(ml_obj: str, ml_result: str, ml_model: str):
    result_file = upscale(ml_obj, ml_result,ml_model)
    print(f'Success\t{result_file}' if result_file else 'Sorry...')
    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()
    for i in range(2):
        example('examples/lama_300px.png',
                'examples/lama_600px.png',
                'models/EDSR_x2.pb')
        print(datetime.datetime.now() - start)
