#  Простейший калькулятор с введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/' and num2 == 0 or num1 == 0:
        return 'Zero division'
    elif operator == '/' and num2 != 0 or num1 != 0:
        return num1 / num2
    elif operator == '0':
        return 'Stop program'


num1 = float(input('Введите число: '))
operator = input('Выберите действие +, -, *, /: ')
num2 = float(input('Введите число: '))
print(calculate(num1, operator, num2))
