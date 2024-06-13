# Создайте класс Example.
# В нём пропишите 3 метода.
# Две переменные задайте как атрибут класса,
# две как атрибут объекта(в init).
# Первый метод: создайте переменную и выведите
# Второй метод: верните сумму 2-ух атрибутов класса
# Третий метод: верните результат возведения первого атрибута объекта во второй атрибут объекта
# Создайте объект класса.
# Напечатайте результат двух методов Напечатайте переменную a.

class Example:
    x = int(input('Введите первое число:'))
    y = int(input('Введите второе число:'))

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method1(self):
        i = int(input('Введите число: '))
        return i

    def method2(self):
        return self.x + self.y

    def method3(self):
        return self.a ** self.b


my_example = Example(2, 4)
print(my_example.method1())
print(my_example.method2())
print(my_example.method3())

# Калькулятор. Создайте класс, где реализованы методы математических операций.
# Каждый метод принимает 2 параметра, первое число и второе число.

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def devide(self, a, b):
        if a == 0 or b == 0:
            return ZeroDivisionError
        else:
            return a / b


calc = Calculator()
a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
print(calc.add(a, b))
print(calc.subtract(a, b))
print(calc.multiply(a, b))
print(calc.devide(a, b))

#  Создайте класс Dog, представляющий собаку.
#  Класс должен иметь атрибуты name (имя собаки) и age (возраст собаки). Реализуйте метод bark(),
#  который выводит на экран сообщение "Гав!".

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Собаку зовут {self.name}, его возраст {self.age}'

    def bark(self):
        return 'Гав'


dog = Dog('Rex', 3)
print(dog.get_info())
print(dog.bark())