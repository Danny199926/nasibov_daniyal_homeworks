#  Даны 2 списка: a = [4,6,'pу','tell',78] b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
#     1)Сложить два списка
#     2) Добавьте число 6 на 3 позицию.
#     3)Удалите все текстовые элементы списка
#     4) Посчитайте количество элементов списка

a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
list1 = a + b
print(list1)
list1.insert(2, 6)
print(list1)
list1 = [x for x in list1 if not isinstance(x, str)]
print(list1)
count = len(list1)
print(count)



