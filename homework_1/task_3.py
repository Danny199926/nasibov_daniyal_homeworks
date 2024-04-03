# Даны два действительных числа. Найти среднее арифметическое и
# среднее геометрическое этих чисел.

import math
a = float(input('Введите число a : '))
b = float(input('Введите число b : '))
average_arithmetic = (a + b) / 2
average_geometric = math.sqrt(a * b)
print(average_arithmetic)
print(average_geometric)
