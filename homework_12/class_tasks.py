# Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.**
import random


def fill_array(start, end):
    array = [random.randint(start, end) for i in range(10)]
    print(array)


start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
fill_array(start, end)


# Написать функцию, которая определяет количество разрядов введённого целого числа.
def digits(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i


num = abs(int(input('Введите число: ')))
print('количество разрядов:', digits(num))

# Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения, которые встречаются в нём более одного раза
input_numbers = list(input('Введите числа: '))
print(input_numbers)
new_list = list(set(filter(lambda i: input_numbers.count(i) > 1, input_numbers)))
print(new_list)
new_str = ''.join(new_list)
print(new_str)

