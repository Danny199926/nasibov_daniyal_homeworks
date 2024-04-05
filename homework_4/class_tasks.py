

 x = int(input('Введите число'))
 if x % 2 == 0:
    print('число является четным')
else:
    print('число является нечетным')

a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a > b and a > c:
    print('a', 'наибольшее число')
elif b > a and b > c:
    print('b', 'наибольшее число')
else:
    print('c', 'наибольшее число')


x = int(input('Введите число'))
if x > 100 or x < -100:
    print('-')
else:
    print('+')

temperature = int(input('Напишите температуру в градусах: '))
if temperature < 0:
    print('на улице холодно')
else:
    print('на улице тепло')

num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
if num1 % num2 == 0:
    print(num1, 'кратно числу', num2)
else:
    print(num1, 'не кратно числу', num2)

x = int(input('Введите число: '))
if x > 0:
    print(x, 'положительное число')
elif x < 0:
    print(x, 'отрицательное число')
else:
    print(x, 'равно 0')

x = int(input('Введите число: '))
if x % 1000 == 0:
    print('millennium')
else:
    print('число', x, 'не делится на 1000 без остатка')



name = input('Введите имя')
x = len(name)
if x <= 3 and x >= 50:
    print('Ошибка ввода')
else:
    print(name)

