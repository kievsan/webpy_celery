from functools import lru_cache

import cv2
from cv2 import dnn_superres

from functools import lru_cache

import os
from app.config import ML_OBJECTS, ML_RESULTS, ML_MODEL


@lru_cache
def get_model(model_path: str):
    """
    :param model_path: путь к ИИ модели
    :return:
    """
    scaler = dnn_superres.DnnSuperResImpl.create()
    scaler.readModel(model_path)
    scaler.setModel('edsr', 2)
    return scaler


def upscale(input_path: str, output_path: str,
            model_path: str = ML_MODEL) -> str:
    """
        :param input_path: путь к изображению для апскейла
        :param output_path:  путь к выходному файлу
        :param model_path: путь к ИИ модели
        :return:
    """

    try:
        image = cv2.imread(input_path)
    except FileNotFoundError as err:
        print(err)
        return ''

    scaler = get_model(model_path)
    result = scaler.upsample(image)

    try:
        cv2.imwrite(output_path, result)
    except OSError as err:
        print(err)
        return ''

    return output_path


def example():
    result_file = upscale(
        os.path.join(ML_OBJECTS, 'lama_300px.png'),
        os.path.join(ML_RESULTS, 'lama_600px.png')
    )
    print(f'Success\t{result_file}' if result_file else 'Sorry...')


if __name__ == '__main__':
    example()
