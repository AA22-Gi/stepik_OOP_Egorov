"""
Класс четырехугольника
Сейчас вам нужно создать класс Quadrilateral(четырехугольник), в котором есть:
    1)  метод __init__, принимающий, как правило, два значения: длину и ширину четырехугольника.
        Но иногда в метод __init__ может передаваться только один аргумент,
        который сразу задает одно значение для ширины и длины (тем самым получается квадрат);

    2)  метод __str__ , который работает следующим образом:
        - если длина и ширина одинаковые, возвращает строку «Квадрат размером <длина>х<ширина>»
        - в противном случае возвращает строку «Прямоугольник размером <длина>х<ширина>»

    3)  метод bool, возвращающий True, если объект является квадратом, и False в противном случае
"""


class Quadrilateral:
    def __init__(self, height, width=None):
        if width is None:
            self.height = height
            self.width = height
        else:
            self.height = height
            self.width = width

    def __str__(self):
        if self.height == self.width:
            return f'Квадрат размером {self.height}х{self.width}'
        return f'Прямоугольник размером {self.height}х{self.width}'

    def __bool__(self):
        return self.height == self.width


if __name__ == '__main__':
    q1 = Quadrilateral(10)
    print(q1)
    assert q1.height == 10
    assert q1.width == 10
    assert bool(q1) is True
    assert q1.__str__() == "Квадрат размером 10х10"
    assert isinstance(q1, Quadrilateral)

    q2 = Quadrilateral(3, 5)
    print(q2)
    assert q2.__str__() == "Прямоугольник размером 3х5"
    assert bool(q2) is not True
    assert isinstance(q2, Quadrilateral)

    q3 = Quadrilateral(4, 7)
    print(q3)
    assert bool(q3) is False
    assert q3.__str__() == "Прямоугольник размером 4х7"
    assert isinstance(q3, Quadrilateral)
