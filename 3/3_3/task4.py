"""
Ваша задача реализовать класс Stack, у которого есть:

    метод __init__ — создаёт новый пустой стек. Параметры данный метод не принимает.
    Создает атрибут экземпляра values, где будут в дальнейшем храниться элементы стека в виде списка (list),
    изначально при инициализации задайте значение атрибуту values, равное пустому списку;

    метод push(item)  — добавляет новый элемент на вершину стека, метод ничего не возвращает;

    метод pop()  — удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент.
    Стек изменяется.
    Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение «Empty Stack»;

    метод peek()  — возвращает верхний элемент стека, но не удаляет его.
    Параметры не требуются, стек не модифицируется.
    Если элементов в стеке нет, распечатайте сообщение «Empty Stack», верните None после этого;

    метод is_empty()  — проверяет стек на пустоту. Параметры не требуются, возвращает булево значение;

    метод size()  — возвращает количество элементов в стеке. Параметры не требуются, тип результата — целое число.
"""
from itertools import count


class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values == list():
            print('Empty Stack')
        else:
            return self.values.pop()

    def peek(self):
        if self.values == list():
            print('Empty Stack')
        else:
            return self.values[-1]

    def is_empty(self) -> bool:
        return self.values == list()

    def size(self) -> int:
        return len(self.values)


if __name__ == '__main__':
    s = Stack()
    assert s.values == []
    assert isinstance(s, Stack)

    s.peek()  # распечатает 'Empty Stack'
    assert s.is_empty() is True
    s.push('cat')
    assert s.size() == 1
    assert s.peek() == 'cat'

    s.push('dog')
    assert s.size() == 2
    assert s.peek() == 'dog'

    s.push(True)
    assert s.size() == 3
    assert s.is_empty() is False

    s.push(777)
    assert s.size() == 4

    assert s.pop() == 777
    assert s.size() == 3

    assert s.pop() is True
    assert s.size() == 2

    s.push(123)
    s.push(123456)
    assert s.peek() == 123456
    assert s.size() == 4

    assert s.pop() == 123456
    assert s.pop() == 123
    assert s.pop() == 'dog'
    assert s.is_empty() is False
    assert s.pop() == 'cat'
    assert s.is_empty() is True

    d = Stack()
    assert d.peek() is None  # Печатает "Empty Stack"
    assert d.pop() is None  # Печатает "Empty Stack"
    d.push('hello')
    assert d.size() == 1
    d.push('world')
    assert d.size() == 2
    assert d.peek() == 'world'
    assert d.pop() == 'world'
    assert d.peek() == 'hello'
