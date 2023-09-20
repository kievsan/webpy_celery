import base64

import cv2 as cv2
from cv2 import dnn_superres
import numpy as np

from functools import lru_cache
import datetime
import os

from flask_celery.settings import ML_PACKAGE, ML_MODEL, ML_EXAMPLES, ML_STORAGE


@lru_cache
def upscaler(model_path: str = ML_MODEL):
    """
        :param model_path: путь к ИИ модели
        :return:
    """
    ml_model = os.path.join(os.path.dirname(__file__), ML_MODEL)
    ml_path = os.path.join(os.path.dirname(__file__), model_path)
    model_path = ml_path if os.path.exists(ml_path) else ml_model
    print(f'start def upscale.upscaler, model:\t{model_path}')  #############
    scaler = dnn_superres.DnnSuperResImpl.create()
    try:
        scaler.readModel(model_path)
        scaler.setModel('edsr', 2)
    except Exception as err:
        print(f'error...{model_path}\n{err}')
        scaler = ''
    return scaler


def imread(image: str, mode='server') -> np.array:
    if mode == 'local':
        print(f'reading...{image}')
        img = cv2.imread(image)
    else:
        nparr = np.fromstring(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def upscale_on_server(img: str, output_path: str):
    image = imread(img)
    print(f'upscaling...')
    result = upscaler().upsample(image)
    print(f'writing...{output_path}')
    cv2.imwrite(output_path, result)


def upscale(input_path: str, output_path: str):
    try:
        with open(input_path, 'rb') as img:
            upscale_on_server(img.read().decode(), output_path)
    except FileNotFoundError as err:
        print(f'error...{output_path}\t{err}')


# def upscale_example(input_path: str, output_path: str) -> str:
#     """
#         :param input_path: путь к изображению для апскейла
#         :param output_path:  путь к выходному файлу
#         :return:
#     """
#
#     # image = cv2.imread(input_path)
#     # result = upscaler().upsample(image)
#     # cv2.imwrite(output_path, result)
#
#     try:
#         print(f'start upscaling...{output_path}')
#         image = imread(input_path, mode='local')
#     except FileNotFoundError as err:
#         print(err)
#         return ''
#
#     result = upscaler().upsample(image)
#
#     try:
#         print(f'writing...{output_path}')
#         cv2.imwrite(output_path, result)
#     except OSError as err:
#         print(err)
#         return ''
#
#     return output_path


def upscale_example(input_path: str,
                    output_filename: str,
                    storage = 'files') -> str:
    """
        :param input_path: путь к изображению для апскейла
        :param output_filename:  имя выходного файлу
        :return:
    """

    # image = cv2.imread(input_path)
    # result = upscaler().upsample(image)
    # cv2.imwrite(output_path, result)

    try:
        print(f'start upscaling...{output_filename}')
        image = imread(input_path, mode='local')
    except FileNotFoundError as err:
        print(err)
        return ''

    result = upscaler().upsample(image)

    try:
        output_path = os.path.join(storage, output_filename)
        print(f'writing...{output_path}')
        cv2.imwrite(output_path, result)
    except OSError as err:
        print(err)
        return ''

    return output_path


def local_example(file_path: str, upscale_filename: str):
    result_file = upscale_example(file_path, upscale_filename, ML_STORAGE)
    print(f'Success\t{result_file}' if result_file else 'Sorry...')


if __name__ == '__main__':
    start = datetime.datetime.now()
    for i in range(2):
        local_example(
            os.path.join(ML_EXAMPLES, 'lama_300px.png'),
            'lama_600px.png'
        )
        print(datetime.datetime.now() - start)
