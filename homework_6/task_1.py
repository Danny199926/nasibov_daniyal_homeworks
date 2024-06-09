# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

import random

chance = 5
while chance > 0:
    nums = random.randint(1, 10)
    nums_of_color = random.randint(1, 2)
    guess_num = int(input('Угадайте число от 1 до 10: '))
    guess_color = int(input('Угадайте цвет красный или черный: '))
    if nums_of_color == 1:
        nums_of_color = 'Красный'
    else:
        'Черный'
    if nums == guess_num and nums_of_color == guess_color:
        print('YOU WIN!!!')
    else:
        print(f'YOU LOSE, номер был {nums}, а цвет {nums_of_color}')
    chance -= 1
    if chance == 5:
        break
print('GAME OVER')





