#  На вход подается непустая строка S. В строке хотя бы два символа.
# 1) В первой строке распечатайте каждый 3-й символ, начиная с нулевого
# (подряд, не разделяя символы пробелами)
# 2) Во второй строке распечатайте первый и последний символы (подряд,
# не разделяя символы пробелами).
# 3) В третей строке распечатайте S в верхнем регистре.
# 4) В четвертой строке распечатайте S в обратном порядке.
# 5) В пятой строке напечатайте True, если все символы в строке S — цифры
# и False в противном случае.

S = 'Сегодня был хороший день'
print(S[::3])
print(S[0] + S[-1])
print(S.upper())
print(S[::-1])