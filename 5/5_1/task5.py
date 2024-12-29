"""
Я создал для вас список shapes, которых хранит в себе экземпляры  различных фигур.
Фигуры перемешаны, созданы в хаотичном порядке

Ваша задача найти и вывести 3 числа в разных строках:
    - на первой строке количество кружочков
    - на второй строке количество фигур, являющихся прямоугольниками
    - на последней строке количество фигур, являющихся многоугольниками.

Прямоугольником являются сами экземпляры класса Rectangle, а также экземпляры квадрата, это класс Square.
Многоугольник это класс Polygon, соответственно он сам и все его дочерние классы будут являться многоугольниками.
"""


class Shape:
    pass


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


class Polygon(Shape):
    pass


class Triangle(Polygon):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


shapes = [
    Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
    Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
    Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
    Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
    Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
    Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
    Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
    Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
    Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
    Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
    Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
    Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
    Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
    Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
]
if __name__ == '__main__':
    circle = [circle for circle in shapes if isinstance(circle, Circle)]
    print(len(circle))

    rectangle = [rectangle for rectangle in shapes if isinstance(rectangle, Rectangle)]
    print(len(rectangle))

    polygon = [polygon for polygon in shapes if isinstance(polygon, Polygon)]
    print(len(polygon))
