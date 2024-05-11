import random

zoo = 'питон', 'слон', 'пингвин'
print(zoo)
new_zoo = 'обезьяна', 'верблюд', zoo
print('кол-во клеток в зоопарке -', len(new_zoo))
print('все животные в новом зоопарке:', new_zoo)
print('животные привезенные из старого зоопарка:', new_zoo[2])
print('последнее животное привезенное из старого зоопарка -', new_zoo[2][2])
print('кол-во животных в новом зоопарке -', len(new_zoo)-1 + len(new_zoo[2]))

# Найти минимальное и максимальное значение кортежа.
x = (1, -22, 33, 44, 5)
in_max = x[0]
in_min = x[0]
for i in x:
    if i > in_max:
        in_max = i
    if i < in_min:
        in_min = i
print(in_max)
print(in_min)

# 2й способ.
a = (1, -22, 33, 44, 5)
list1 = list(a)
list1.sort()
print(f'мин-ое значение - {list1[0]}, макс-ое значеие - {list1[-1]}')


# Даны два кортежа. Требуется объединить их между собой:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
print(tuple1 + tuple2)

# В кортеже целых чисел найдите максимальный и минимальный элементы, а также осуществите их обмен.
tuple3 = (1, 2, -20, 29, -93, -13, 12)
min_element = tuple3[0]
max_element = tuple3[0]
for i in tuple3:
    if i < min_element:
        min_element = i
    elif i > max_element:
        max_element = i
print(f'мин. элемент - {min_element}')
print(f'макс. элемент - {max_element}')
tuple_list = list(tuple3)
for i in range(len(tuple_list)):
    if tuple_list[i] == min_element:
        tuple_list[i] = max_element
    elif tuple_list[i] == max_element:
        tuple_list[i] = min_element
tuple3 = tuple(tuple_list)
print('кортеж поосле обмена -', tuple3)


# В список, сгенерированный случайным образом, добавить введенный пользователем элемент.
list1 = [random.randint(1, 50) for i in range(10)]
print(list1)
new_element = int(input('Введите новый элемент: '))
list1.append(new_element)
print(list1)


# В список, сгенерированный случайным образом, добавить введенный пользователем элемент
# на указаннную позицию.
list2 = [random.randint(1, 10) for i in range(10)]
print(list2)
element = input('Введите элемент который хотите добавить: ')
position = int(input('Введите позицию: '))
list2.insert(position, element)
print(list2)


# Имеются два списка, сгенерированные случайным образом.
# Добавьте в конец первого списка все элементы второго списка.
list3 = [random.randint(1, 100) for i in range(5)]
print(list3)
list4 = [random.randint(1, 100) for i in range(5)]
print(list4)
list3.extend(list4)
print(list3)

# Из заранее сформированного списка следует удалить элемент, веденный
# пользователем
list5 = [1, 4, 5, 3]
deleted_el = int(input('Введите элемент который хотите удалить: '))
list5.remove(deleted_el)
print(list5)

# Из исходного списка следует удалить элемент, позицию которого указал пользователь.
list6 = [random.randint(1, 100) for i in range(5)]
deleted_element = int(input(f'Введите позицию которую хотите удалить из списка {list6}: '))
list6.pop(deleted_element)
print(list6)

# В кортеже целых чисел вычислите произведение отрицательных элементов,
# имеющих нечетные индексы
import random
x = tuple(random.randint(-50, 10) for i in range(10))
print(x)
prod = 1
for i in range(1, len(x), 2):
    if x[i] < 0:
        prod *= x[i]
        print(x[i])
print(prod)

# Заполниете один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от -5 до 0. Объедините 2 кортежа с помощью оператора +,
# создав тем самым третий кортеж. С помощью метода кортежа count() определите в нём количество нулей.
# Выведите на экран третий кортеж и количество нулей в нём
a = tuple(random.randint(0, 5) for i in range(5))
print(a)
b = tuple(random.randint(-5, 0) for i in range(5))
print(b)
x = a + b
print(f'у кортежа {x} кол-во нулей: {x.count(0)}')

# Вывести данные кортежа без скобок, через запятую. Обязательно элементы кортежа - строки
tuple5 = 'green', 'yellow', 'blue', 'white'
print(','.join(tuple5))

# Сгенерируйте 2 кортежа случайными числами в диапозоне от 10-90.
# Количество элементов в кортеже 10.
# Определить:
#     1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран
#        (Сумма больше в кортеже - ...)
#     2) Вывести на экран порядковые номера минимальных элементов этих кортежей
e = tuple(random.randint(10, 90) for i in range(10))
print(e)
r = tuple(random.randint(10, 90) for i in range(10))
print(r)
sum_e = 0
sum_r = 0
for i in e:
    sum_e += i
for j in r:
    sum_r += i
if sum_e > sum_r:
    print(f'сумма кортежа {e} больше суммы кортежа {r}')
elif sum_e < sum_r:
    print(f'сумма кортежа {r} больше суммы кортежа {e}')
else:
    print(f'сумма кортежа {e} равна сумме кортежа {r}')
print(f'мин-ое значение кортежа {e}: {min(e)} ')
print(f'макс-ое значение кортежа {r}: {max(r)}')

