#   В РАЗРАБОТКЕ
from pprint import pprint

import requests
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
        # получаем файл
        image = requests.get(url)
        # тестируем
        status_code = image.status_code
        assert status_code == 200
        print(image.status_code,
              image.request.method
              )         ###################
        # image.content
        break

    elif response_status == 'FAILURE':
        print('Что-то пошло не так')
        break

