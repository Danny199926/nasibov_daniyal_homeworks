#  Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
#  если год високосный, и False иначе.
import math
import random


def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


input_year = int(input('Введите год: '))
print(is_year_leap(input_year))


# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры.
def square(side):
    perim = 4 * side
    area = side * side
    diag = side * math.sqrt(2)
    return perim, area, round(diag, 2)


print(square(4))


#  Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#  и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#  Номер месяца вводить с клавиатуры.

def season(num_of_month):
    if num_of_month in [12, 1, 2]:
        return 'Зима'
    elif num_of_month in [3, 4, 5]:
        return 'Весна'
    elif num_of_month in [6, 7, 8]:
        return 'Лето'
    elif num_of_month in [9, 10, 11]:
        return 'Осень'
    else:
        return 'Вы ввели число несуществующего месяца'


input_num_of_mn = int(input('Введите число месяца: '))
print(season(input_num_of_mn))


#  Функция, вычисляющая среднее арифметическое элементов списка. Список должен состоять из случайных чисел,
#  длинной 10 элементов.
def average(list1):
    result = sum(list1) / len(list1)
    print(result)


list1 = [random.randint(1, 100) for i in range(10)]
print(list1)
average(list1)


# Создайте функцию, добавьте в неё локальное значение.
# Сделайте так, чтобы другая функция принимала это значение в качестве аргумента.
def multiply():
    num1 = 2
    return num1


def inner(num2):
    num2 = int(input('Введите второе число: '))
    return num1 * num2


def multiply(num1):
    return num1(4)


def inner(num2):
    return num2 * 2


print(multiply(inner))


# Функция для определения того, каким является число: положительным, отрицательным или нулем
def type_of_num(num1):
    if num1 > 0:
        return f'число {num1} является положительным'
    elif num1 < 0:
        return f'число {num1} является отрицательным'
    else:
        return f'число {num1} является нулем'


num1 = int(input('Введите число: '))
print(type_of_num(num1))
