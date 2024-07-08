import requests

params = {'q': 'python'}
responds = requests.get('https://www.google.ru/search', params=params)
#print(responds)
#print(responds.status_code)
#print(responds.headers)
#print(responds.text)

with open('google.html', 'w', encoding='utf-8')as file:
    file.write(responds.text)