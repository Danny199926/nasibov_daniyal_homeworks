# Квадраты всех целых чисел от 1 до 10.
number = 1
while number <= 10:
    square = number ** 2
    print(f'квадрат числа {number} равен {square}')
    number += 1

# Перемножить все чётные значения в диапазоне от 0 до 125; результат вывести на экран.
result = 1
number = 0
while number <= 125:
    if number % 2 == 0:
        if number != 0:
            result *= number
    number += 1
print(f'результат умножения четных чисел {result}')

# Вывести числа от 1 до 15 в порядке убывания
number = 15
while number >= 1:
    print(number)
    number -= 1

# Пользователь вводит два числа c клавиатуры, необходимо вывести на экран все отрицательные числа, лежащие между ними.
# Например пользователь ввел -5 и 3, на экране вывелось -4, -3, -2, -1

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
i = num1 + 1
while i < num2 and i < 0:
    print(i)
    i += 1


# Необходимо, чтоб программа выводила на экран вот такую последовательность
# (не использовать готовый список): 7 14 21 28 35 42 49 56 63 70 77 84 91 98 Добавить в список и найти его длинну.
order = " "
counter = 7
while counter <= 98:
    order += str(counter) + " "
    counter += 7
print(order)
order_list = order.split()
print(len(order_list))

# Вася начал тренироваться бегать. В первый день день он пробежал 1 км.
# Каждый последующий день он увеличивал пройденное расстояние на 10% от предыдущего дня.
# Сколько дней Васе понадобится, чтобы пробежать в сумме хотя бы 10 км?
distance = 1
days = 1
while distance < 10:
    distance += distance * 0.10
    days += 1
print(f'Васе понадобится {days} дней, чтобы пробежать 10 км')

# Необходимо с помощью цикла while вывести данную последовательность чисел:
# 1 2 4 8 16 32 64 128 256 512
i = 1
while i <= 512:
    print(i)
    i = i + i


# Калькулятор
while True:
    num1 = float(input('Введите число: '))
    operator = input('Выберите оператор(+, -, *, /, **, //, %): ')
    num2 = float(input('Введите число: '))
    if operator in '+':
        print(num1 + num2)
        break
    elif operator in '-':
        print(num1 - num2)
        break
    elif operator in '*':
        print(num1 * num2)
        break
    elif operator in '/':
        print(num1 / num2)
        break
    elif operator in '**':
        print(num1 ** num2)
        break
    elif operator in '//':
        print(num1 // num2)
        break
    elif operator in '%':
        print(num1 % num2)
        break
print('end of program')


