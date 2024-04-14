# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

from random import randint
start = True
chance = 0
while start:
    number_of_guess = (1, 11)
    number_of_color = (1, 3)
    user_number = int(input('Угадайте число от 1 до 10: '))
    user_color = int(input('Угадайте цвет (красный или черный): '))
    chance += 1
    if number_of_color == 1:
        number_of_color = 'красный'
    else:
        number_of_color = 'черный'
    if number_of_guess == user_color and number_of_color == user_number:
        print(f'Поздравляю, вы угадали. Загаданное число было {number_of_guess}, а цвет - {number_of_color}')
    else:
        print(f'Вы не угадали')
    if chance == 5:
        break
print(f'Игра окончена')





