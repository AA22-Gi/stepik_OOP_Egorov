"""
Создайте класс Triangle, в котором реализованы следующие методы

    1) метод __init__, принимающий три стороны треугольника

    2) метод is_exists, который отвечает на вопрос, существует ли треугольник с текущими сторонами
    Треугольник существует, если каждая сторона треугольника меньше суммы двух других сторон.

    3) метод is_equilateral, который проверяет, является ли треугольник равносторонним
    Треугольник называется равносторонним, если у него все стороны равны

    4) метод is_isosceles, который проверяет, является ли треугольник равнобедренным и существующим.
    Треугольник называется равнобедренным, если у него две стороны равны
"""


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self) -> bool:
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a:
            return True
        return False

    def is_equilateral(self) -> bool:
        if self.a == self.b == self.c:
            return True
        return False

    def is_isosceles(self) -> bool:
        if self.is_exists() and (self.a == self.b or self.b == self.c or self.a == self.c):
            return True
        return False