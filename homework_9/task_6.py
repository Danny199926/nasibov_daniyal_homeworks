# Создать произвольный словарь 2. Добавить новый элемент с ключом типа str и значением
# типа int 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу 5. Удалить элемент по ключу
# 6. Получить список ключей словаря.

dict1 = {'blue': 'синий', 'red': 'красный'}
dict1['cars'] = 3
print(dict1)
dict1[tuple('yellow')] = ['желтый']
print(dict1)
print(dict1['cars'])
dict1.pop('blue')
print(dict1)
print(list(dict1.keys()))
