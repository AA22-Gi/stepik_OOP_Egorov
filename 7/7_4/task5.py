"""
Бесконечная арифметическая прогрессия
Создайте класс InfinityIterator, который реализует бесконечный итератор.
Он должен возвращать элементы арифметической прогрессии с шагом 10.
Начальное значение арифметическое прогрессии по умолчанию равно 0,
но при инициализации класса InfinityIterator может быть передано другое значение.

Каждый член арифметической прогрессии равен предыдущему, сложенному с одним и тем же числом d.
В нашем случае значение d=10.

Вот пример работы итератора InfinityIterator:
#>>> a = iter(InfinityIterator())
#>>> next(a)
0
#>>> next(a)
10
#>>> next(a)
20
#>>> next(a)
30
Или если использовать InfinityIterator в цикле for со стартовым значением 7

for i in InfinityIterator(7):
    print(i)
# будет печатать на экран
7
17
27
37
....
"""


class InfinityIterator:
    def __init__(self, start=0, step=10):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        self.start += self.step
        return current


if __name__ == '__main__':
    a = iter(InfinityIterator(7))
    for i in range(5):
        print(next(a))
