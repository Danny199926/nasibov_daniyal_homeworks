# Создать множество. Создать неизменяемое множество. Выполнить операцию объединения
# созданных множеств. Выполнить операцию пересечения созданных множеств.

set1 = {1, 2, 3, 4, 5}
set2 = tuple([4, 5, 6])
union = set1.union(set(set2))
print(union)
intersection = set1.intersection(set2)
print(intersection)
