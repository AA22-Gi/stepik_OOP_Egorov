"""
В некоторых языках программирования существует структура данных под названием вектор.
    Vector — это контейнер, который упорядочивает элементы данного типа в виде линейной последовательности.
    Он обеспечивает быстрый произвольный доступ к любому элементу
    и позволяет динамически добавлять элементы в последовательность и удалять их.

Давайте создадим класс Vector,
экземпляры которого будут представлять собой контейнеры для хранения только целых чисел.

Ваша задача — создать класс Vector, который хранит в себе коллекцию целых чисел.
У класса Vector должны быть реализованы:

    1)  метод __init__, принимающий произвольное количество аргументов.
        Среди всех переданных аргументов необходимо оставить только целые числа
        и сохранить их в экземпляр в виде списка;

    2)  переопределить метод __str__ так, чтобы экземпляр класса Vector отображался следующим образом:
        - «Вектор(<value1>, <value2>, <value3>, ...)», если вектор не пустой.
        При этом значения должны быть упорядочены по возрастанию
        (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);

        - «Пустой вектор», если наш вектор не хранит в себе значения
"""


class Vector:

    def __init__(self, *args):
        self.args = args

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args):
        self.__args = sorted([i for i in args if type(i) == int])

    def __str__(self):
        if not self.args:
            return 'Пустой вектор'
        return f'Вектор({', '.join([str(i) for i in self.args])})'


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    print(str(v1))
    print(isinstance(v1, Vector))

    v2 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
    print(str(v2))
