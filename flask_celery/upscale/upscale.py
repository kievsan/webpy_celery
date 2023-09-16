import base64

import cv2
import numpy
# import numpy as np
# from cv2 import dnn_superres

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
    scaler = cv2.dnn_superres.DnnSuperResImpl.create()
    scaler.readModel(model_path)
    scaler.setModel('edsr', 2)
    return scaler


def imread(image: str, mode='server') -> numpy.array:
    if mode == 'local':
        img = cv2.imread(image)
    else:
        nparr = numpy.fromstring(image, numpy.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def upscale_on_server(img: str, output_path: str) -> numpy.array:
    image = imread(img)
    print(f'upscaling...')
    result = upscaler().upsample(image)
    print(f'writing...{output_path}')
    cv2.imwrite(output_path, result)
    return result


def upscale(input_path: str, output_path: str):
    try:
        with open(input_path, 'rb') as img:
            print(f'reading...{input_path}')
            result = upscale_on_server(img.read().decode())

    except FileNotFoundError as err:
        print(f'error...{output_path}\t{err}')


def upscale_example(input_path: str, output_path: str) -> str:
    """
        :param input_path: путь к изображению для апскейла
        :param output_path:  путь к выходному файлу
        :return:
    """
    try:
        image = imread(input_path, mode='local')
    except FileNotFoundError as err:
        print(err)
        return ''

    result = upscaler().upsample(image)

    try:
        print('writing...')
        cv2.imwrite(output_path, result)
    except OSError as err:
        print(err)
        return ''

    return output_path


def local_example(ml_file_path: str, ml_result: str):
    result_file = upscale_example(ml_file_path, ml_result)
    print(f'Success\t{result_file}' if result_file else 'Sorry...')


if __name__ == '__main__':
    start = datetime.datetime.now()
    for i in range(2):
        local_example(
            os.path.join(ML_EXAMPLES, 'lama_300px.png'),
            os.path.join(ML_STORAGE, 'lama_600px.png')
        )
        print(datetime.datetime.now() - start)
