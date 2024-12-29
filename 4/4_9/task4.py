"""
Правим класс Vector. Часть 4.
Добавьте к реализации класса Vector метод __delitem__,
который будет удалять из вектора все упоминания переданного значения.

К примеру, если имеется вектор  a = Vector(3, 4, 5, 5, 6, 6)
то операция del a[5] должна удалить два элемента, значения которых равны 5.

Если переданное значение отсутствует в векторе,
нужно вызвать исключение ValueError('Значение <value> отсутствует в векторе')
"""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

    def __delitem__(self, key):
        if key in self.values:
            self.values = [value for value in self.values if key != value]
        else:
            raise ValueError(f'Значение {key} отсутствует в векторе')


if __name__ == '__main__':
    v1 = Vector(5, 5, 5, 4, 4, 3)
    print(v1)
    del v1[4]
    print(v1)
    del v1[5]
    print(v1)
    try:
        del v1[10]
    except ValueError as e:
        print(e)
    print()

    v1 = Vector(5, 6, 7, 8, 9, 5)
    del v1[6]
    del v1[9]
    print(v1)
    del v1[5]
    print(v1)
