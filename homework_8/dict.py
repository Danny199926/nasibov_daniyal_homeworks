# Объединение словарей
dict1 = {'cat1': 'кот', 'dog1': 'собака'}
dict2 = {'cat2': '2', 'dog2': 'собака2'}
a = dict1 | dict2
print(a)

# Методы
new_dict = {'cat': 'кот', 'dog': 'собака'}
value_cat = new_dict.get('cat')  # Получение значения по ключу
print(value_cat)
object_keys_and_values = new_dict.items()
print(object_keys_and_values)
x = list(object_keys_and_values)
print(x.pop(1))
object_keys = new_dict.keys()
print(object_keys)
object_values = new_dict.values()
print(object_values)
new_dict.pop('cat')
print(new_dict)
new_dict1 = {'bird': 'птица'}
new_dict.update(new_dict1) # Добавление
print(new_dict)
new_dict['zebra'] = 'Зебра'
print(new_dict)
new_dict.popitem() # Удаление последнего элемента
print(new_dict)
a = [1, 2, 3]
b = [4, 5, 6]
c = dict(zip(a, b)) # Преобразование двух списков в словарь
print(c)
#for i in c:
#    print(f'ключ {i}')
#    print(f'значение {c[i]}')
for key in c.keys():
    print(key)
for value in c.values():
    print(value)