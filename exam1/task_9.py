# 9.Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.
list1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
list2 = []
for i in list1:
    if ' ' in i:
        list2.append(i)
print(list2)