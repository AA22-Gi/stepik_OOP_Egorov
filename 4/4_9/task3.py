"""
Правим класс Vector. Часть 3
Давайте вернем в вектор обычное обращение по индексу и добавим возможность обращаться к нашему вектору еще и по ключу.
Ключом мы будем считать любое строковое значение. При обращении по ключу вы должны найти длину ключа и,
исходя из этого значения, достать элемент, располагающийся на данном индексе.

Например, обращение a['home'] должно вернуть элемент по индексу четыре, так как длина строки home равна 4.
Индексация элементов должна начинаться с единицы.

Во всех ситуациях, когда индекс выходит за пределы вектора,
необходимо вызвать исключение IndexError('Индекс <index> находится за пределами вектора')
"""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if isinstance(item, str):
            item = len(item)
        if 0 < item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")


if __name__ == '__main__':
    v = Vector(3, 655, 323, 672, 11, 6)
    print(v[1])  # 3
    print(v[2])  # 655
    print(v['cat'])  # 323
    print(v['park'])  # 672
    try:
        print(v[''])
    except IndexError as e:
        print(e)
    print()

    v = Vector(5, 7, 8, 9, 2, 3)
    print(v['q'])  # 5
    print(v['_+'])  # 7
    print(v['567'])  # 8
    print(v['!@#$'])  # 9
    print(v['abba'])  # 9
    print(v['qwerty'])  # 3
    try:
        print(v['abracadabra'])
    except IndexError as e:
        print(e)