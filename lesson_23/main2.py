x = 2
y = 1
assert y != 0
print(x + y)


def avg(ranks):
    assert len(ranks) != 0
    return round(sum(ranks) / len(ranks), 2)


my_ranks = [23, 76, 43]
print(f'среднее значение {avg(my_ranks)}')

