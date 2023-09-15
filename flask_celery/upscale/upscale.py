import cv2
from cv2 import dnn_superres

from functools import lru_cache
import datetime
import os

from flask_celery.settings import ML_MODEL, ML_EXAMPLES, ML_STORAGE


@lru_cache
def upscaler(model_path: str = ML_MODEL):
    """
        :param model_path: путь к ИИ модели
        :return:
    """
    scaler = dnn_superres.DnnSuperResImpl.create()
    scaler.readModel(model_path)
    scaler.setModel('edsr', 2)
    return scaler


def upscale(input_path: str, output_path: str) -> str:
    """
        :param input_path: путь к изображению для апскейла
        :param output_path:  путь к выходному файлу
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
    result = upscaler().upsample(image)

    try:
        print('writing...')
        cv2.imwrite(output_path, result)
    except OSError as err:
        print(err)
        return ''

    return output_path


def example(ml_obj: str, ml_result: str):
    result_file = upscale(ml_obj, ml_result)
    print(f'Success\t{result_file}' if result_file else 'Sorry...')


if __name__ == '__main__':
    start = datetime.datetime.now()
    for i in range(2):
        example(os.path.join(ML_EXAMPLES, 'lama_300px.png'),
                os.path.join(ML_STORAGE, 'lama_600px.png'))
        print(datetime.datetime.now() - start)
