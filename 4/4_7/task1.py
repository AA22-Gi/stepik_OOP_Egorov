"""
y = ax**2 + bx + c
Давайте воссоздадим эту формулу в виде класса QuadraticFunction, в котором есть:
    1)  метод __init__, который должен сохранять в экземпляр класса три атрибута: a, b и c;
    2)  метод __call__ , который принимает аргумент x, подставляет его в формулу выше,
        находит значение и возвращает его в качестве результата
"""


class QuadraticFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


if __name__ == '__main__':
    f = QuadraticFunction(2, 5, 7)
    assert f(1) == 14
    assert f(-3) == 10
    assert f(2) == 25
    assert f(5) == 82

    f_2 = QuadraticFunction(-1, 2, 4)
    assert f_2(5) == -11
    assert f_2(2) == 4
    assert f_2(-3) == -11
    assert f_2(1) == 5
    print('Good')