from math import sqrt


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

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

    def get_distance(self, coordinate):
        if not isinstance(coordinate, Point):
            print('Передана не точка')
            return None
        elif isinstance(coordinate, Point) and hasattr(self, ('x' and 'y')) and hasattr(coordinate, ('x' and 'y')):
            try:
                res = sqrt((self.x - coordinate.x) ** 2 + (self.y - coordinate.y) ** 2)
                return res
            except Exception as e:  # Перехватывает любое исключение
                print(f'Ошибка: {e}')
        else:
            print('Координаты не заданы')
            return None


if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    p1.set_coordinates(1, 2)
    p2.set_coordinates(4, 6)
    p1.display()
    p2.display()
    print(p1.get_distance(p2))
    print(p2.get_distance(p1))
    print()

    p1 = Point()
    p2 = Point()
    print(p1.get_distance(p2))
    p1.set_coordinates(1, 2)
    print(p1.get_distance(p2))
    p2.set_coordinates(4, 6)
    print(p1.get_distance(p2))
    print()

    p1 = Point()
    p1.set_coordinates(1, 2)
    print(p1.get_distance(100))
    print(p1.get_distance([1, 2, 3]))
    print(p1.get_distance(Point()))
