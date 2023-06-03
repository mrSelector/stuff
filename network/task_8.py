"""Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний).
 Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та
    друкувати на консоль статус-код, заголовки та тіло відповіді."""

import requests
from requests.exceptions import HTTPError


def http_request_client(url, method, data=None):
    result = None
    try:
        if method == 'GET':
            result = requests.get(url)
        elif method == 'POST':
            result = requests.post(url, data=data)
        elif method == 'PUT':
            result = requests.put(url, data=data)
        elif method == 'DELETE':
            result = requests.delete(url)
    except HTTPError as error:
        print(error)
    print(f'Status_code: {result.status_code}')
    for header_key, header_value in result.headers.items():
        print(f'{header_key} : {header_value}')
    print(f'Body: {result.text}')


url = 'https://jsonplaceholder.typicode.com'
method = 'GET'

http_request_client(url, method)
