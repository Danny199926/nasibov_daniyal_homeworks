# запись csv
import csv

import pandas

name_1 = 'Petya'
name_2 = 'Misha'
with open('task1.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([name_1, name_2])

# ОбЪединение данных изначально в список
list1 = ['Petya', 'Misha']
with open('task1.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(list1)

# записываем заголовки для таблиц
with open('task2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('login', 'password'))

# Создаем список с логинами и паролями
data = [
    ['login1', 'password1'],
    ['login2', 'password2'],
    ['login3', 'password3']
]
for element in data:
    with open('task2.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(element)

with open('task2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

data = [
    ('login', 'password'),
    ['login1', 'password1'],
    ['login2', 'password2'],
    ['login3', 'password3']
]
with open('task3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('task3.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = [
    ['Логин', 'пароль'],
    ['Логин2', 'пароль2']
]
with open('task4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('task4.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('task4.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

result = pandas.read_csv('task3.csv')
print(result)
