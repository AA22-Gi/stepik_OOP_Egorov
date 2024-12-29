"""
Правим класс Vector. Часть 2

Вам необходимо вновь изменить реализацию класса Vector из урока.
Я оставил ее для вас в том виде, в котором она была в теории.

Теперь нужно сделать обратную реализацию: в качестве индекса будет поступать значение,
а возвращать нужно его позицию. Если значение в векторе присутствует несколько раз,
то необходимо вернуть список, в котором содержатся все индексы, где находится данное значение.
Если значение отсутствует в векторе, нужно поднимать исключение ValueError('В векторе отсутствует значение <value>')

Индексация должна начинаться с единицы.
"""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if self.values.count(item) == 0:
            raise ValueError(f'В векторе отсутствует значение {item}')
        elif self.values.count(item) == 1:
            return self.values.index(item) + 1
        else:
            return [index + 1 for index, value in enumerate(self.values) if value == item]


if __name__ == '__main__':
    v1 = Vector(3, 655, 323, 672, 11, 6)
    print(v1[655])  # 2
    print(v1[672])  # 4
    print(v1[3])  # 1
    try:
        print(v1[10])
    except ValueError as e:
        print(e)
    print()

    v1 = Vector(5, 5, 5, 4, 4, 3)
    print(v1[4])  # [4, 5]
    print(v1[5])  # [1, 2, 3]
    print(v1[3])  # 6
    try:
        print(v1[2])
    except ValueError as e:
        print(e)
