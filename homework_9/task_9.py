# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.

string = "attention"
new_result = tuple(dict.fromkeys(string))
print(new_result)
