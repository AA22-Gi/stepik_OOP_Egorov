"""
Продолжаем серию задач про точки.
Теперь ваша задача — реализовать метод get_point_with_max_distance,
который найдет среди всех созданных на данный момент экземпляров точку,
которая больше остальных удалена от начала координат.

Если есть несколько точек, находящихся на одинаковом максимальном расстоянии от начала координат,
нужно выбрать ту, которая находится выше остальных на координатной плоскости.
Если и таких точек несколько, покажите первую.

Гарантируется, что точки создаются с уникальными координатами, а значит,
не будет ситуации, когда две точки имеют одинаковые координаты.

В качестве результата своей работы метод get_point_with_max_distance
должен вызвать метод display у найденной точки.
"""

from math import sqrt


class Point:
    all_points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.all_points.append(self)

    def get_distance_to_origin(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            distance = sqrt(self.x ** 2 + self.y ** 2)
            return distance
        else:
            return None

    def display(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            print(f'Point({self.x}, {self.y})')
        else:
            print('Координаты не заданы')


    def get_point_with_max_distance(self):
        self.big_point = max(Point.all_points, key=lambda x: (x.get_distance_to_origin(), x.y))
        return self.big_point.display()




if __name__ == '__main__':
    p1 = Point(6, 8)
    p2 = Point(8, 6)

    p2.get_point_with_max_distance()