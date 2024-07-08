import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
API_TOKEN = '23c30b0dd0de015f74603f43ea680a46'
params = {'q': 'Махачкала', 'appid': API_TOKEN, 'units': 'metric'}
responce = requests.get(url, params=params)
#print(responce.status_code)
#print(responce.headers)
#print(responce.json())
data = responce.json()
print(data)
print(data.get('main').get('temp_min'))
print(data.get('main').get('temp_max'))
print(data.get('sys').get('country'))
print(data.get('name'))
print(data.get('wind').get('speed'))