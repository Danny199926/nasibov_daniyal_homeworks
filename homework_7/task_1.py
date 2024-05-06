# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента
import random

list1 = [random.randint(1, 100) for i in range(11)]
print(list1)
for i in range(1, len(list1)):
    if list1[i] > list1[-1]:
        print(list1[i])



