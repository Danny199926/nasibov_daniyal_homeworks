import random

# Проверить, есть ли у последователльности дубликаты?
numbers = [random.randint(0, 50) for i in range(10)]
print(numbers)
set_number = set(numbers)
print(set_number)
if len(numbers) != len(set_number):
    print('yes, they have')
else:
    print('no, they dont have')

#  Напишите программу, которая создает пустое множество
#  и заполняет его 10 случайными целыми числами от 1 до 20.
#  Затем выведите это множество на экран.
set1 = set()
while len(set1) < 10:
    set1.add(random.randint(1, 20))
print(set1)

#  Вам необходимо создать 2 множества а затем
#  из двух этих множеств получить третье множество таким образом,
#  чтобы новое множество содержало только те элементы, которые есть в обоих исходных множествах.
set2 = {1, 2, 5, 6}
set3 = {2, 4, 2, 3}
set4 = set2.intersection(set3)
print(set4)

# Напишите программу, которая проверяет, является ли одно множество подмножеством другого множества.
set5 = {1, 2, 3}
set6 = {1, 2, 3, 4, 5}
x = True
for items in set5:
    if items not in set6:
        x = False
print(x)

# Напишите программу, которая будет генерировать множество,
# # а на выходе программа  возвращает список, содержащий все элементы этого множества, умноженные на 2.
set7 = {i for i in range(10)}
print(set7)
list1 = list(set1)
for i in set7:
    list1[i] = i * 2
print(list1)

# Создайте два множества из списка слов "apple", "banana", "orange", "grape", "kiwi" и "banana".
# Выведите на экран разность этих множеств.
list2 = ['apple', 'banana', 'orange', 'grape', 'kiwi']
list3 = ['banana']
set8 = set()
for i in list2:
    set8.add(i)
set9 = set()
for j in list3:
    set9.add(j)
difference = set8 - set9
print(difference)

# Напишите программу, которая удаляет все дубликаты из списка и создает из него множество.
even_numbers = [random.randint(0, 10) for i in range(10)]
print(even_numbers)
x = list(set(even_numbers))
print(x)

# Сгенерируйте два множества. Программа должна вернуть новое множество,
# содержащее все элементы из первого множества, которых нет во втором.
set10 = {random.randint(1, 100) for i in range(10)}
print(set10)
set11 = {random.randint(1, 100) for j in range(10)}
print(set11)
diff = set()
for item in set10:
    if item not in set11:
        diff.add(item)
print(diff)


