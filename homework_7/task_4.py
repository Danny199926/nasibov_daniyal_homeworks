# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс
# этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
import random

#list1 = [random.randint(1, 100) for i in range(11)]
#print(list1)
#max_el = max(list1)
#print(max_el)
#print(list1.index(max_el))


list1 = [random.randint(1, 100) for i in range(11)]
print(list1)
index_of_max = 0
for i in range(len(list1)):
    if list1[i] > list1[index_of_max]:
        index_of_max = i
print(list1[index_of_max], index_of_max)

