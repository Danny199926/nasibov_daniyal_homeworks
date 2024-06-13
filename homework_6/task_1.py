# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

import random

chance = 5
while chance > 0:
    number = random.randint(1, 10)
    color = random.randint(1, 2)
    if color == 1:
        color = 'Красный'
    else:
        color = 'Черный'
    guess_num = int(input('Угадайте число от 1 до 10: '))
    guess_color = int(input('Угадайте цвет красный или черный: '))
    if number == guess_num and color == guess_color:
        print('YOU WIN!!!')
    else:
        print(f'YOU LOSE, номер был {number}, а цвет {color}')
    chance -= 1
    if chance == 5:
        break
print('GAME OVER')





