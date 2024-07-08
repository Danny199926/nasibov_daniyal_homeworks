# Установить Postman и попробовать отправить запросы для получения ответа через него
import requests
# Get
response = requests.get('https://reqres.in/api/users')
print(f'Статус: {response.status_code}')
print(f'Тело: {response.text}')

# Post
url = 'https://reqres.in/api/users'
data = {'name': 'Morpheus', 'job': 'Leader'}
response = requests.post(url, data=data)
print(f'Статус: {response.status_code}')
print(f'Тело: {response.text}')

# Put
url = 'https://reqres.in/api/users/2'
data = {'name': 'Updated name', 'job': 'Updated job'}
response = requests.put(url, data=data)
print(response.status_code)
print(response.json())

