# Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей, и выведите количество таких элементов. Крайние элементы
# списка никогда не учитываются, поскольку у них недостаточно соседей.
import random

list1 = [random.randint(1, 100)for i in range(11)]
print(list1)
count = 0
for i in range(1, len(list1) - 1):
    if list1[i] > list1[i-1] and list1[i] > list1[i+1]:
        print(list1[i])
        count += 1
print(count)
