# Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны(в классе написать проверку на валидность данных)

class Calculator:
    def check_validity(self, a, b):
        try:
            a, b = float(a), float(b)
        except ValueError:
            return False, None, None
        return True, a, b

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


calculator = Calculator()

while True:
    a = input('Введите первое число: ')
    x = input('Введите операцию(+, -, *, / или 0): ')
    if x == '0':
        break
    b = input('Введите второе число: ')
    valid, a, b = calculator.check_validity(a, b)
    while not valid:
        print('Оба значения должны быть числовыми')
        a = int(input('Введите первое число: '))
        b = int(input('Введите первое число: '))
        valid, a, b = calculator.check_validity(a, b)
    if x == '+':
        print(calculator.add(a, b))
    elif x == '-':
        print(calculator.subtract(a, b))
    elif x == '*':
        print(calculator.multiply(a, b))
    elif x == '/':
        print(calculator.devide(a, b))
    else:
        print('Неверный знак')
