# 6. Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
x = [1, 5, 2, 9, 2, 9, 1]
for i in x:
    if x.count(i) == 1:
        print(f'число не имеющее пары = {i}')
