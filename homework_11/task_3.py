# Если в функцию передаётся кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и
# чисел в нём. Число - кол-во нечётных цифр. Строка - количество букв. Сделать проверку со всеми этими случаями

def type_smth(smth):
    if isinstance(smth, tuple):
        return f'сумма длины слов кортежа,', sum([len(word) for word in smth])
    elif isinstance(smth, list):
        return f'кол-во букв и чисел,', len([i for i in smth if str(i).isdigit() or str(i).isalpha()])
    elif isinstance(smth, int):
        return f'кол-во нечетных чисел,', len([digit for digit in str(smth) if digit in '13579'])
    elif isinstance(smth, str):
        return f'кол-во букв,', len(smth)
    else:
        return 'type is not defined'


print(type_smth(('hello', 'world')))
print(type_smth(['hey', 'where', 'are', 'you', 2, 3]))
print(type_smth(126579))
print(type_smth('hungry'))
