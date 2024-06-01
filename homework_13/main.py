# 1 способ открытия файла
file = open('task1.txt', 'r')
print(file)
# 1 способ чтения файла
print(*file)
file.close()
# 2 способ открытия файла
with open('task1.txt', 'r') as file:
    print(*file)
    print(file.read(3))
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readlines())
    line_numbers = [4, 7]
    for i, line in enumerate(file):
        if i in line_numbers:
            print(line)
        elif i > 8:
            break

with open('task2.txt', 'w', encoding='utf-8') as file:
    file.write('Привет мир')
    file.writelines(['привет1', 'привет2', 'привет3'])

with open('task2.txt', 't') as file:
    line = file.read()
    print(line)
    numbers = []
    for i in line:
        if i.isdigit():
            numbers.append(i)
    print(numbers)

with open(r'C:\Users\User\PycharmProjects\homework_13\new_directory\test.path.txt', 'r') as file:
    print(file.read())

