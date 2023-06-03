# Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів
# та обробити відповіді. Необхідно попрактикуватися з urllib та бібліотекою requests.
# Рекомендується спочатку спробувати виконати запити, використовуючи urllib, а потім спробувати
# реалізувати те саме, використовуючи requests.

from urllib import request
import requests

response = request.urlopen('https://jsonplaceholder.typicode.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
print(response.headers)
print(response.getheaders())
print(response.headers.get('Content-Type'))
print(response.getheader('Report-To'))

"""Бібліотека requests"""


response1 = requests.get('https://jsonplaceholder.typicode.com')
print(response1.status_code)
print(response1.content)
print(response1.text)
print(response1.headers['Content-Type'])
print(response1.headers['Report-To'])


response2 = requests.put('https://jsonplaceholder.typicode.com')
response3 = requests.post('https://jsonplaceholder.typicode.com')
response4 = requests.delete('https://jsonplaceholder.typicode.com')
