"""
Класс PowerTwo

Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени (2**0 = 1).
Внутри класса реализуйте:

    1)  метод __init__. Он должен принимать одно положительное число - степень двойки,
        до которой нужно итеририроваться включительно (см пример ниже)

    2)  методы __iter__ и __next__ для итерирования по степеням двойки

for i in PowerTwo(4): # итерируемся до 4-й степени двойки
    print(i)
# Цикл выше печатает следующие числа
1
2
4
8
16
"""


class PowerTwo:
    def __init__(self, value: int):
        self.value = value
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.value:
            raise StopIteration
        else:
            degree = self.count
            self.count += 1
            return 2 ** degree


if __name__ == '__main__':
    numbers = PowerTwo(2)

    assert hasattr(numbers, '__next__') is True
    assert hasattr(numbers, '__iter__') is True

    iterator = iter(numbers)
    print('Элементы итератора PowerTwo(2)')
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    try:
        print(next(iterator))
        raise ValueError('Не реализовали StopIteration')
    except StopIteration:
        pass

    print('-' * 15)
    print('Элементы итератора PowerTwo(20)')
    for i in PowerTwo(20):
        print(i)
