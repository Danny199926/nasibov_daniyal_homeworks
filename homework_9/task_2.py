# Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами.
# Выведите полученный словарь на экран.

d = {'1': 0, '2': 0, '3': 0}
print(d)

a = ['1', '2', '3']
b = [0, 0, 0]
c = dict(zip(a, b))
print(c)

e = dict([('1', 0), ('2', 0), ('3', 0)])
print(e)
