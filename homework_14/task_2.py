# Создайте функцию, которая принимает на вход список словарей и сохраняет его в CSV файл.
# Каждый словарь представляет собой строку данных, а ключи словарей - названия столбцов.
import csv

dict1 = [
    {'name': 'Sean Strickland', 'age': 30, 'sex': 'm'},
    {'name': 'Dominick Cruz', 'age': 35, 'sex': 'm'},
    {'name': 'Marge Simpson', 'age': 41, 'sex': 'w'},
]


def dicts_csv(dict1):
    with open('task2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dict1[0].keys())
        for i in dict1:
            writer.writerow(i.values())


dicts_csv(dict1)
