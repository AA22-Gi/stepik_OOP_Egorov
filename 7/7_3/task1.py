"""
Создайте  класс SequenceIterable,
который принимает контейнер данных в виде списка в момент инициализации и сохраняет его в атрибуте ЭК.

SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
Вы должны научить класс SequenceIterable создавать итерируемый объект

container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)

# Печатает
1
5
4
6
43
True
hello

Необходимо только написать реализацию класса SequenceIterable
"""


class SequenceIterable:
    def __init__(self, data: list):
        self.data = data

    def __iter__(self):
        return iter(self.data)


if __name__ == '__main__':
    container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
    for i in container:
        print(i)
