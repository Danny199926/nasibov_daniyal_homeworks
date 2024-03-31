# способы создания списка
list1 = []
list2 =list()

animals_names = ['cat', 'dog', 'panda']
numbers = []

name = 'Danny'
list3 = list(name)
print(list3)

# Индексы
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0])
print(numbers[-1])

# методы
new_list = [1, 2, 3, 4]
new_list.append(5)  # добавление в конец списка
print(new_list)
new_list.insert(0, 10) # добавление на указанную позицию элемент
print(new_list)
new_list.remove(10) # удаление по имени элемента
print(new_list)
new_list.pop(-1)
print(new_list)
del_value = new_list.pop(-1) # удаление по индексу + возвращает удаленный элемент
print(new_list, f'удаленное значение из списка {del_value}')
print(new_list.count(6))

# изменить элемент в списке
x = [1, 2, 3, 4]
x[0] = 'hello'
print(x)

# разница между изменяемыми и неизменяемыми???
x_list1 = [1, 2, 3, 4]
y_list1 = x_list1
print(y_list1)
x_list1.append(5)
print(x_list1)
print(y_list1)

# неизменяемые
x = 2
y = x
y += 2
print(y)
print(x)


x = [1, 2, 5, 7, 'cat']
for i in x:
    print(i)

# C клавиатуры вводим начало, и конец и шаг последовательности. Необходимо вывести на
# на экран данную последовательности чисел.

start = int(input('Введите начало последовательности: '))
end = int(input('Введите конец последовательности: '))
step = int(input('Введите шаг последовательности: '))
for i in range(start, end, step):
   print(i)

# Вывести длину списка ['cat', 'dog', 'flowers', 1, 2, 3]

list1 = ['cat', 'dog', 'flowers', 1, 2, 3]
print(len(list1))

# Задан список - [1, 2, 5, 6, 7, 8]. Необходимо вывести его сумму и произведение.

list1 = [1, 2, 5, 6, 7, 8]
sum_num = 0
prod = 1
for i in list1:
    sum_num += i
    prod *= i
    print(sum_num)
    print(prod)

# Вывести на экран все числа в диапазоне от 54 до 9184 кратные 5.
for i in range (54, 9184):
    if i % 5 == 0:
       print(i)

# Посчитать сколько раз встречается определенная цифра(цифра - это от 0 до 9) в списке чисел.
# Искомая цифра задаются с клавиатуры.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
digit = int(input('Введите цифру от 0 до 9: '))
count = numbers.count(digit)
print(f'цифра {digit} встречается в списке {count} раз. ')
