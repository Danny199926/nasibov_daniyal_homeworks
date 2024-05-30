def call_with_five(function):
    return function(5)


def add_one(x):
    return x + 1


print(call_with_five(add_one))


def multiply(num1):
    def inner(num2):
        return num1 * num2

    return inner


print(multiply(1)(4))


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper()


@uppercase_decorator
def say_hi():
    return 'всем привет'


print(say_hi)

double = lambda x: x * 2
print(double(5))


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
