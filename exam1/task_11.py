# 11. Дан список чисел, необходимо удалить все вхождения числа 20 из него.
list1 = [20, 49, 20, 84, 67, 20]
for i in list1:
    if i == 20:
        list1.remove(i)
print(list1)