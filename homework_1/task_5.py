# Вычислить сумму цифр случайного трёхзначного числа.

import random
ran_num = random.randint(100,999)
print("Случайное число:", ran_num)
ran_num = str(ran_num)
ran_num1 = int(ran_num[0])
ran_num2 = int(ran_num[1])
ran_num3 = int(ran_num[2])
sum_ran_num = ran_num1 + ran_num2 + ran_num3
print("Сумма:", sum_ran_num)
