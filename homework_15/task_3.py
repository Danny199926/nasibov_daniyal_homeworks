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

def validate(func):
    def wrap(a, b):
        if a == str or b == str:
            raise ValueError
        return func(a, b)

    return wrap


@validate
def sum(a, b):
    return a + b


try:
    a = int(input('Введите число: '))
    b = int(input('Введите второе число: '))
    print(sum(a, b))
except ValueError:
    print('error')



