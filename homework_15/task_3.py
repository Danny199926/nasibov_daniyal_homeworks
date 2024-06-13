# Задача на декоратор
#
# метод sum(a, b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы не числовые параметры(например строка)
# пример:
#
# @validate_int_parameters
# def sum(a,b)`
#
# sum(3, "1") => ошибка
# sum(4, 2) = > 6

class Decorator:
    def sum(self, a, b):
        if a == str or b == str:
            raise ValueError
        else:
            return a + b


dec = Decorator()
try:
    a = int(input('Введите число: '))
    b = int(input('Введите второе число: '))
    print(dec.sum(a, b))
except ValueError:
    print('error')


