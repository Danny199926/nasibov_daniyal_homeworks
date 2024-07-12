import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://github.com/login'
auth_url = 'https://github.com/session'
user = UserAgent().random

data = {
    'login': 'nasdanny50@gmail.com',
    'password': 'Demonvtapo4kax',
    'authenticity_token': ''
}
headers = {
    'user-agent': user
}

with requests.Session() as session:
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    find_token = soup.find('input', {'name': 'authenticity_token'})
    token = find_token.get('value')
    data.update({'authenticity_token': token})
    print(data)
    response = session.post(auth_url, headers=headers, data=data)
    html_page = response.text
    with open('github_html', 'w', encoding='utf-8') as file:
        file.write(html_page)




