import requests
import datetime
import time

response = requests.post('http://127.0.0.1:5000/example/',
    json={
        "filename": "lama_300px.png"
    })

resp_data = response.json()
task_id = resp_data['task_id']
print(response.status_code, resp_data)

while True:
    time.sleep(1)
    response = requests.get(f'http://127.0.0.1:5000/tasks/{task_id}')
    status_code = response.status_code
    resp_data = response.json()
    print(status_code, resp_data)
    assert status_code == 200
    response_status = resp_data.get('status')
    if response_status == 'SUCCESS':
        url = resp_data.get('link')
        image = requests.get(url)
        status_code = image.status_code
        assert status_code == 200
        break
    elif response_status == 'FAILURE':
        print('Что-то пошло не так')
        break

