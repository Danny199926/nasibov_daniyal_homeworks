# 8. Вывести на экран числа от 0 до 50, кроме 35.
numbers = [i for i in range(0, 50)]
for i in numbers:
    if i == 35:
        numbers.remove(i)
print(numbers)
