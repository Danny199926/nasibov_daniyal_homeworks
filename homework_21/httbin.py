import requests
from fake_useragent import UserAgent

#user = UserAgent().random
#url = 'https://httpbin.org/headers'

#headers = {
#    'Accept': 'application/json',
#    'User-agent': user
#}

#responce = requests.get(url, headers=headers)
#print(responce.json())

#url = 'https://httpbin.org/post'
#data = {
#    'custname': 'Danny',
#    'custtel': '89289867940',
#    'custmail': 'nasdanny50@gmail.com',
#    'size': 'small',
#    'topping': 'bacon',
#    'delivery': '19:00',
#    'comments': 'faster'
#}

#user = UserAgent().random
#headers = {
#    'User-agent': user
#}
#responce = requests.post(url, headers=headers, json=data)
#print(responce.status_code)
#print(responce.json())

# Get
url = 'https://reqres.in/api/users?page=2'
responce = requests.get(url)
print(responce.json())

# Create
data = {
    'name': 'morpheous',
    'job': 'leader'
}
url = 'https://reqres.in/api/users'
responce = requests.post(url, data=data)
print(responce.status_code)
print(responce.json())

# Update put & patch
data = {
    'name': 'morpheous',
    'job': 'zion resident'
}
url = 'https://reqres.in/api/users/2'
responce = requests.patch(url, data=data) # responce = requests.put(url, data=data)
print(responce.status_code)
print(responce.json())

# Login successfull
data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
url = 'https://reqres.in/api/login'
responce = requests.post(url, data=data)
print(responce.status_code)
print(responce.json())

# Delete
url = f'https://reqres.in/api/users/2{responce.json()['id']}'
responce = requests.delete(url)
print(responce.status_code)


