# Создать произвольный словарь 2. Добавить новый элемент с ключом типа str и значением
# типа int 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу 5. Удалить элемент по ключу
# 6. Получить список ключей словаря.

set1 = {'blue': 'синий', 'red': 'красный'}
set1['cars'] = 3
print(set1)
set1[tuple('yellow')] = ['желтый']
print(set1)
print(set1['cars'])
set1.pop('blue')
print(set1)
print(list(set1.keys()))
