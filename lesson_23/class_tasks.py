# Написать функцию, которая будет заполнять список степенями числа 2 (от 2^1 до 2^n). n - целое число.

def fill_powers_of_two(n):
    assert isinstance(n, int) and n > 0
    powers = []
    for i in range(1, n + 1):
        power = 2 ** i
        powers.append(power)
    return powers


print(fill_powers_of_two(3))


#  """Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()"""

def add_len_to_keys(dictionary):
    new_dict = {}
    for key in dictionary.keys():
        new_key = f'{key}{len(key)}'
        new_dict[new_key] = dictionary[key]
    return new_dict


original_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print(original_dict)
modified_dict = add_len_to_keys(original_dict)
print('измененный словарь:', modified_dict)

assert modified_dict == {'test4': 'test_value', 'europe6': 'eur', 'dollar6': 'usd', 'ruble5': 'rub'}
print('Проверка пройдена')


# """Ввести строку. Если длина строки больше 10 то создать новую строку с 3 восклицательными
# знаками и
# вывести на экран. Если у нас меньше чем 10 то вывести второй символ строки"""

def process_string(input_string):
    assert len(input_string) <= 10
    if len(input_string) > 10:
        new_string = '!!!'
        print(new_string)
    else:
        print(input_string[1])


user_input = input('Введите строку: ')
process_string(user_input)
