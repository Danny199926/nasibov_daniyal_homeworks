import random

list_of_elements = [1, 2, 3, 4, 5, 'b', 'a', 'c']
list_of_elements.append(6)
print(list_of_elements)
x = [7, 8, 9]
list_of_elements.extend(x)
print(list_of_elements)
list_of_elements.remove(9)
print(list_of_elements)
list_of_elements.pop(10)
print(list_of_elements)
list_of_elements.insert(0, 10)
print(list_of_elements)

numbers = []
strings = []
for i in list_of_elements:
    if isinstance(i, int):
        numbers.append(i)
    if isinstance(i, str):
        strings.append(i)
numbers.sort(reverse=True)
strings.sort()
new_list = numbers + strings
print(new_list)
new_list.reverse()
print(new_list)
new_list[0] = 'hello world python'
print(new_list)

# Дан произвольный список, представить его в обратном порядке
x = [1, 2, 3, 4, 5, 6, 7]
x.reverse()
print(x)

# Дан список с числами и в нем есть цифра 20. Поменять 20 на 200.
list2 = [1, 2, 3, 4, 5, 20]
list2[5] = 200
print(list2)

# Напишите программу, которая выводит каждый второй элемент списка.
list3 = [i for i in range(10)]
print(list3[1::2])

# Сгенерируйте список, который должен составлять 10 элементов.
# Найдите сумму всех его четных элементов. (встроенную функцию для нахождения суммы использовать нельзя)
list6 = [random.randint(1, 10) for i in range(11)]
sum_elements = 0
for i in list6:
    if i % 2 == 0:
    sum_elements += i
print(sum_elements)

# Найти совпадающие элементы двух списков. a = [5,[1,2],2,'r',4,'ee'] b = [4,'we','ee',3,[1,2]]
# Эти значения записать в новый список
a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)

# Напишите программу для удаления элементов с четными индексами из списка
list7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list7:
    index = list7.index(i)
    if i % 2 == 0:
        list7.pop(index)
print(list7)

list10 = [i for i in range(10) if i % 2 != 0]
print(list10)

# Напишите программу для нахождения второго наименьшего элемента в списке
lol = [random.randint(1, 100) for i in range(10)]
print(lol)
lol.sort()
print(lol)
print(lol[1])

# Список из 7 цифр. Если чётных цифр в нём больше, то найти сумму всех цифр,
# если нечётных больше то найти произведение 1, 3 и 6 элемента.
list4 = [random.randint(1, 15) for i in range(7)]
x1 = 0
x2 = 0
summ = 0
prod = 1
for i in list4:
    if i % 2 == 0:
        x1 += 1
    else:
        x2 += 1
print(f'четные - {x1}, нечетные - {x2}')
if x1 > x2:
    for i in list4:
        summ += i
        print(f'сумма {summ}')
else:
    prod = list4[0] * list4[2] * list4[5]
    print(f'произведение {prod}')

