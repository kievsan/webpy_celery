import requests
import datetime
import time


test_request = 'http://127.0.0.1:5000/simple/'
request_number = 10
task_sleep = '5 сек'
header = f'\nЦЕЛЬ:\t{request_number} задач в очереди\n' \
         f'\n\tДлительность каждой задачи:\tчуть больше {task_sleep}\n'

def accept_simple_result(rule: str, task_id: str) -> bool:
    time.sleep(0.2)
    response = requests.get(f'{rule}{task_id}')
    status_code = response.status_code
    resp_data = response.json()
    # print(status_code, resp_data)       ######################
    assert status_code == 200
    response_status = resp_data.get('status')
    if response_status == 'SUCCESS':
        print(f"{resp_data.get('phrase')}\t-->\t{resp_data.get('pun')}\n")
    elif response_status == 'FAILURE':
        print("Что-то пошло не так")
    return response_status in ['SUCCESS', 'FAILURE']


def check_tasks(rule: str, func, checklist: list[str]) -> list[str]:
    return list(id for id in checklist if not (func(rule, id)))


def start_requests(rule: str, msg: str, ddos: int) -> list[str]:
    checklist = list()
    for request_number in range(ddos):
        test_data = {'message': f'{msg} {request_number}'}
        response = requests.post(rule, json=test_data)
        resp_data = response.json()
        task_id = resp_data.get('task_id')
        checklist.append(task_id)
        # print(response.status_code, resp_data)      ####################
        # checklist = check_tasks(rule, accept_simple_result, checklist)
    return checklist


print(header)
checklist = start_requests(test_request, 'simple greeting', request_number)

print(f'\n{len(checklist)} задач в очереди\n')

start = datetime.datetime.now()
while True:
    checklist = check_tasks(test_request, accept_simple_result, checklist)
    tasks_left = len(checklist)
    if tasks_left:
        print('\n', tasks_left, 'tasks left after',
              datetime.datetime.now() - start, '\n')
    else:
        break

print('0 tasks left after', datetime.datetime.now() - start)
