# Определить, является ли год високосным.

import calendar

year = int(input('Введите год: '))
if calendar.isleap(year):
     print(year, 'год високосный.')
else:
     print(year, 'год не високосный.')
