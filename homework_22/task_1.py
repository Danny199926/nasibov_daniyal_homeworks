# С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами, только те телефоны,
# которые можно добавить в корзину.
# записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
# Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость)
import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.21vek.by/mobile/iphone_12_mini/'


response = requests.get(url)
response.raise_for_status()
print(response)

soup = BeautifulSoup(response.content, 'html.parser')


products = soup.find_all('div', class_='product-card')


data = []


for product in products:
    name = product.find('a', class_='product-card__title').text.strip()

    gb = product.find('span', class_='product-card__characteristics').text.strip()

    price = product.find('span', class_='product-card__price-value').text.strip()

    data.append([name, gb, price])

with open('iphone_12_mini.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Название', 'GB', 'Цена'])
    writer.writerows(data)

print("Данные успешно записаны в файл iphone_12_mini.csv")