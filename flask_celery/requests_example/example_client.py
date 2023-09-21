#   В РАЗРАБОТКЕ

import requests
import os
import re

import datetime
import time

server = 'http://127.0.0.1:5000'
response = requests.post(f'{server}/example/',
    json={
        "filename": "lama_300px.png"
    })

resp_data = response.json()
task_id = resp_data['task_id']
print(response.status_code, resp_data)

while True:
    # получаем Задачу (указываем правило для ссылки на файл)
    response = requests.get(f'{server}/tasks/{task_id}',
                            params={'file_rule': 'example',})
    status_code = response.status_code
    resp_data = response.json()
    print(status_code, resp_data)   ###################
    assert status_code == 200

    # Ждем и Проверяем готовность результатов
    time.sleep(2)
    response_status = resp_data.get('status')
    if response_status == 'SUCCESS':
        # получаем ссылку на файл
        url = resp_data.get('link')
        # запрашиваем файл
        image = requests.get(url, stream=True)
        # проверяем ответ
        status_code = image.status_code
        assert status_code == 200
        print(image.status_code,
              image.request.method
              )         ###################

        # читаем и сохраняем файл
        name = re.findall('filename=(.+)',
                          image.headers['Content-Disposition'])[0]
        destination = os.path.join(os.path.expanduser('~'), name)
        print('writing...', destination)    ##############
        with open(destination, 'wb') as fp:
            while True:
                chunk = image.raw.read(1024)
                if not chunk:
                    break
                fp.write(chunk)
        print('writing...SUCCESS')    ##############
        break

    elif response_status == 'FAILURE':
        print('Что-то пошло не так')
        break

