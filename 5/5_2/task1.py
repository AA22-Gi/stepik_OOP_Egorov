"""
Давайте усовершенствуем наш класс MyList
    class MyList(list):
        pass
У списков есть полезный метод .remove(value), который позволяет удалить значение value один раз из списка.
Если value отсутствует в списке, происходит исключение ValueError.

Ваша задача создать метод .remove_all(value), который будет удалять сразу все значения, которые равны value.
Если value отсутствует в списке, ничего делать не нужно. Метод в конце своей работы должен вернуть None
"""


class MyList(list):
    def remove_all(self, value):
        while value in self:
            self.remove(value)
        return None


if __name__ == '__main__':
    s = MyList([1, 2, 3, 2, 1, 2])
    assert s == [1, 2, 3, 2, 1, 2]
    s.remove_all(2)
    assert s == [1, 3, 1]
    s.remove_all(1)
    assert s == [3]
    s.remove_all(5)
    assert s == [3]
    s.remove_all(3)
    assert s == []

    k = MyList([0] * 20)
    assert k == [0] * 20
    k.remove_all(7)
    assert k == [0] * 20
    k.append(8)
    k.append(0)
    k.append(2)
    k.remove_all(0)
    assert k == [8, 2]
    print('Good')
