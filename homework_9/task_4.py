# На вход программы подается словарь a = {1:10, 2:20, 3:30},
# необходимо получить список произведения ключа на значение.

a = {'1': 10, '2': 20, '3': 30}
list1 = []
for key, values in a.items():
    list1.append(key * values)
print(list1)
