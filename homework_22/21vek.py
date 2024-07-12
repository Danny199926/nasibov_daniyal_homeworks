import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user = UserAgent().random
url = 'https://www.21vek.by/mobile/iphone_15pro/'
headers = {
    'user-agent': user
}
response = requests.get(url, headers=headers)
#with open('21vek_html', 'w', encoding='utf-8') as file:
#    file.write(responce.text)

# tasks
soup = BeautifulSoup(response.text, 'lxml')
#main_block = soup.find('div', {'data-testid': 'product-list'})
#print(main_block)
#block_phone = main_block.find('div', {"data-testid": 'product-8560605'})
# print(block_phone)
#block_phone_2 = block_phone.find('p', {"data-testid": 'card-info'})
# print(block_phone_2)
#title_phone = block_phone_2.find('a', {'data-testid': 'card-info-a'}).text
# print(title_phone)
# price
#block_price = block_phone.find('section', {'data-testid': 'card-price'})
# print(block_price)
#price = block_price.find('p', {"data-testid": 'card-current-price'}).text
#print(title_phone, price)
