# Напишите программу, которая запрашивает у пользователя два числа и выполняет деление первого числа на второе.
# В случае, если второе число равно нулю, программа должна обработать исключение деления на ноль и вывести сообщение
# "Деление на ноль невозможно".
import math

try:
    n1 = int(input('number 1: '))
    operator = input('use operator(-, +, *, /): ')
    n2 = int(input('number 2: '))
    if operator in '+':
        print(n1 + n2)
    elif operator in '-':
        print(n1 - n2)
    elif operator in '*':
        print(n1 * n2)
    elif operator in '/':
        print(n1 / n2)
except ZeroDivisionError:
    print('error')
finally:
    print('the end')

# Даны действительные числа x и y. Получить
x = int(input('Введите число: '))
y = int(input('Введите число: '))
a = (abs(x) - abs(y)) / (1 + (x * y))
print(a)

# Даны катеты прямоугольного треугольника. Найти его гипотенузу и
# площадь.
z = float(input('Введите значение первого катета: '))
b = float(input('Введите значение первого катета: '))
c = math.sqrt(a * a + b * b)
s = 0.5 * a * b
print(f'Гипотенуза: {c}')
print(f'площадь: {s}')

# Создать переменные a, b, c и присвоить им значения 9, 17 и 5 соответственно.
# Проверить выполнение следующих условий:
# a больше b
# a не равно разности b и c
# b равно сумме a и c
# c меньше или равно сумме a и b
# a меньше b, но больше c
# b больше a или b больше c
a = 9
b = 17
c = 5
print(a > b)
print(a != (b - c))
print(b == (a + c))
print(c <= (a + b))
print(a < b and a > c)
print(b > a or b > c)

# Перевести строку в список по пробелу "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "lists", "they", "are", "my", "favorite"]
str1 = 'Robin Singh'
s = str1.split()
print(s)
str2 = 'I love arrays they are my favorite'
a = str2.split()
x = str(a).replace('arrays', 'lists')
print(x)

# Дан список ["I", "love", "lists", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list1 = ['I', 'love', 'lists', 'they', 'are', 'my', 'favorite']
str_list = str(list1).replace('lists', 'arrays')
print(str_list)

# Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем.
list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, -1, 0, -9, 4, -5]
for i in (list1, list2, list3):
    i.sort()
print(list1[1])
print(list2[1])
print(list3[1])

# Дан список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’.
# Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.
list1 = ['red', 'green', 'white', 'black', 'pink', 'yellow']
lst = []
lst.append(list1[0])
lst.append(list1[4])
lst.append(list1[5])
print(lst)

# Даны два целых числа m и n. Напишите программу,
# которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.
m = int(input('Введите число: '))
n = int(input('Введите число: '))
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

# С помощью цикла while просите пользователя решить пример, пока он не введет правильный ответ.
answer = 4
chance = 3
while chance > 0:
    user_answer = int(input('Решите пример: 2 + 2 = ?: '))
    if user_answer == answer:
        print('Right!')
        break
    else:
        chance -= 1
        print('not correct')
        if chance == 0:
            print('end of program')

# Дан список чисел [1, 2, 3, 20, 30, 45, 20, 100, 20], необходимо удалить все вхождения числа 20 из него.
list1 = [1, 2, 3, 20, 30, 45, 20, 100, 20]
for i in range(list1.count(20)):
    list1.remove(20)
print(list1)

# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
list1 = []
for i in range(100):
    list1.append(0)
list1[0] = 1
list1[-1] = 1
print(list1)

# Сформировать возрастающий список из чётных чисел (количество элементов 45)
list1 = [i for i in range(45) if i % 2 == 0]
print(list1)

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list1 = []
for i in a:
    if i < 5:
        list1.append(i)
print(list1)

# Заполнить список степенями числа 2 (от 2^1 до 2^n)
n = int(input('Введите число: '))
x = [2 ** i for i in range(1, n + 1)]
print(x)

# Дан словарь с числовыми ключами и значениями.
# Необходимо их все ключи перемножить а значения сложить и вывести на экран.
set1 = {1: 2, 2: 3, 3: 4}
prod = 1
sum_of = 0
for i in set1.keys():
    prod *= i
for i in set1.values():
    sum_of += i
print(f'ппроизведение ключей - {prod}')
print(f'сумма значений - {sum_of}')

# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
set1 = {i: i ** 3 for i in range(1, 11)}
print(set1)

# Напишите программу,
# которая получает на вход две строки с перечислением интересов и хобби двух пользователей,
# и вычисляет процент совпадения
interests = 'хоккей, футбол, шахматы теннис'
interests2 = 'футбол, волейбол, теннис, гонки'
list4 = interests.split(', ')
list5 = interests2.split(', ')
common_interests = []
for i in list4:
    if i in list5:
        common_interests.append(i)
total = list4.copy()
for i in list5:
    if i not in list4:
        total.append(i)
percent = len(common_interests) / len(total) * 100
print(f'процент совпадения интересов - {percent}%')

