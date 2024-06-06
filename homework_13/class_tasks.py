# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел.
with open('task.txt', 'r') as file:
    result = file.read()
print(result)
sum_el = 0
new_res = result.replace('_', ' ')
print(new_res)
for i in result:
    if i.isdigit():
        sum_el += int(i)
print(sum_el)

# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.
with open('task2.txt', 'r') as file:
    result = file.read().splitlines()
    print(result)
    numbers = []
    letters = []
    for i in result:
        if i.isdigit():
            numbers.append(int(i))
        elif i.isalpha():
            letters.append(i)
numbers.sort()
letters.sort(key=len)
numbers.extend(letters)
print(numbers)



