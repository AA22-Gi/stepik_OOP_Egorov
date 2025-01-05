"""
Обходим стэк
Вспоминаем задачу про структуру LIFO

Теперь научим его итерироваться.
У вас имеется готовый код класса Stack (см. ниже в блоке кода).
Обратите внимание на реализацию метода __iter__
    def __iter__(self):
    return StackIterator(self)

Значит класс Stack логику перебора элементов делегирует классу StackIterator.
Ваша задача реализовать итератор в классе StackIterator, который обходит элементы стека сверху вниз

Необходимо написать только реализацию класса StackIterator
"""


class StackIterator:
    def __init__(self, stack):
        self.stack = stack.items  # Сохраняем ссылку на элементы стека
        self.index = len(self.stack) - 1  # Начинаем с индекса верхнего элемента стека

    def __iter__(self):
        return self  # Возвращаем сам итератор

    def __next__(self):
        if self.index < 0:  # Проверяем, не вышли ли мы за пределы стека
            raise StopIteration  # Останавливаем итерацию, если элементы закончились
        else:
            item = self.stack[self.index]  # Получаем элемент по текущему индексу
            self.index -= 1  # Переходим к следующему элементу (вниз по стеку)
            return item  # Возвращаем текущий элемент


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return StackIterator(self)


stack = Stack()

stack.push(100)
stack.push(True)
stack.push('hello')
stack.push('world')

# Используем итератор для обхода стека
for item in stack:
    print(item)
