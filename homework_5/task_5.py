# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны
# быть равны единице

list = []
for i in range(100):
    list.append('0')
list[0] = 1
list[-1] = 1
print(list)