# Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару
import random

list1 = [random.randint(-100, 100) for i in range(11)]
print(list1)
for i in range(1, len(list1)):
    if list1[i] > 0 and list1[i-1] > 0 or list1[i] < 0 and list1[i-1] < 0:
        print(list1[i], list1[i-1])
