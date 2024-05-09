# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент
#этого списка.

import random
x = [random.randint(1, 100) for i in range(10)]
print(x)

index_of_min = 0
index_of_max = 0
for i in range(1, len(x)):
    if x[i] > x[index_of_max]:
        index_of_max = i
    if x[i] < x[index_of_min]:
        index_of_min = i
x[index_of_min], x[index_of_max] = x[index_of_max], x[index_of_min]
print(x)


list6 = [-5, -3, 8, -2, 10, 15, 3, 9, 200, 909, -1099]
min_index = list6.index(min(list6))
max_index = list6.index(max(list6))
list6[min_index], list6[max_index] = list6[max_index], list6[min_index]
print(list6)
