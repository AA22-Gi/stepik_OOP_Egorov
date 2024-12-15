"""
Создайте класс Rectangle, у которого есть:

     ➖ метод __init__, принимающий 2 аргумента: длину и ширину;

     ➖ свойство area, которое возвращает площадь прямоугольника;

     ➖ свойство perimeter, которое возвращает периметр прямоугольника.
"""


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__area = None
        self.__perimeter = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value
        self.area = None
        self.__perimeter = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.length * self.width
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = (self.length + self.width) * 2
        return self.__perimeter


if __name__ == '__main__':
    r1 = Rectangle(5, 10)
    assert isinstance(r1, Rectangle)
    assert r1.area == 50
    assert isinstance(type(r1).area, property), 'Вы не создали property area'

    r2 = Rectangle(15, 3)
    assert isinstance(r2, Rectangle)
    assert r2.area == 45
    assert isinstance(type(r2).area, property), 'Вы не создали property area'

    r3 = Rectangle(43, 232)
    assert r3.area == 9976
    print('Good')
