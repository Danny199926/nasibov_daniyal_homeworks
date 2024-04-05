# 1)Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. - результат число
# Если нечётное, то заменить его на 1 в списке. - результат список
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list = [15, 48, 'hello', 6, 19, 'world']
print(list)
for i in range(len(list)):
    element = list[i]
    if isinstance(element, int):
        if element % 2 == 0:
            sum_digits = element // 10 + element % 10
            print(f'так как элемент списка четное число, то сумма его цифр равно {sum_digits}')
        else:
            element == 1
            print(f'так как элемент списка нечетное число, {element} заменить 1')
    elif isinstance(element, str):
        vowels = 0
        consonants = 0
        for i in element.lower():
            if i in 'aeiouy':
                vowels += 1
            else:
                consonants += 1
                print(f'так как элемент списка слово, то количество гласных в нем: {vowels}, согласных: {consonants}')

