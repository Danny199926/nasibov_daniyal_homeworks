import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user = UserAgent().random
url = 'https://browser-info.ru/'
headers = {
    'user-agent': user
}
responce = requests.get(url, headers=headers)
html_page = responce.text
#print(html_page)

soup = BeautifulSoup(html_page, 'lxml')
main_block = soup.find('div', id='tool_padding')
#print(main_block)
block_js = main_block.find('div', id='javascript_check')
#print(block_js)
list_elements = block_js.find_all('span')
#print(list_elements)
js = list_elements[0].text
status = list_elements[1].text
#print(f'{js} - {status}')

#tasks
flash_block = soup.find('div', id='flash_version')
#print(flash_block)
block_flash = flash_block.find_all('span')
#print(block)
list_flash = block_flash[0].text
stat = block_flash[1].text
#print(f'{list_flash} - {stat}')

user_block = soup.find('div', id='user_agent')
block_user_agent = user_block.text
#print(block_user_agent)

info = soup.find('div', id='left_opisanie')
#print(info)
h2 = info.find('h2')
#print(h2.text)

