# Вычислить сумму цифр случайного трёхзначного числа.

import random

number = random.randint(100, 999)
print(number)
print(sum((number // 100, number // 10 % 10, number)))