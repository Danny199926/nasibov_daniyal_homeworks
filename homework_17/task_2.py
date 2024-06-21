# Класс «Прямоугольный треугольник»
# Класс содержит два действительных числа – стороны треугольника. и включает
# следующие методы:
# увеличение/уменьшение размера стороны на заданное количество процентов;
# вычисление радиуса описанной окружности,
# вычисление периметра,
# определение значений углов.

import math


class RightTriangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def resize(self, side, percentage):
        if side == "side1":
            self.side1 *= (1 + percentage / 100)
        elif side == "side2":
            self.side2 *= (1 + percentage / 100)

    def calculate_circumradius(self):
        hypotenuse = math.sqrt(self.side1 * 2 + self.side2 * 2)
        return hypotenuse / 2

    def calculate_perimeter(self):
        hypotenuse = math.sqrt(self.side1 * 2 + self.side2 * 2)
        return self.side1 + self.side2 + hypotenuse

    def calculate_angles(self):
        angle1 = math.degrees(math.atan(self.side2 / self.side1))
        angle2 = 90 - angle1
        return angle1, angle2


# Пример использования
triangle = RightTriangle(3, 4)

print("Радиус описанной окружности:", triangle.calculate_circumradius())
print("Периметр:", triangle.calculate_perimeter())
angle1, angle2 = triangle.calculate_angles()
print("Угол 1:", angle1, "градусов")
print("Угол 2:", angle2, "градусов")

# Увеличение стороны side1 на 20%
triangle.resize("side1", 20)

# Вывод новых значений сторон
print("Новые стороны:", triangle.side1, triangle.side2)
