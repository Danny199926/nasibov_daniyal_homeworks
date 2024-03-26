#  Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и
# вывести на экран. Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

name = "Apples, Oranges, Pears, Bananas, Berries"
name_split = name.split(",")
print(name_split)
name_join = " ".join(name_split)
print(name_join)