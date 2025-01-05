"""
Создайте объект итератор FibonacciIterator, который умеет выдавать последовательность Фибоначчи из n чисел.
Число n поступает при инициализации класса FibonacciIterator.

Будем считать, что последовательность Фибоначчи следующая: 0, 1, 1, 2, 3, 5, 8, 13, 21 и т.д.
Каждое следующее число получается суммой двух предыдущих.

Пример использования:
fibonacci_iter = FibonacciIterator(7)

for number in fibonacci_iter:
    print(number)
# Печатает
0
1
1
2
3
5
8
"""


class FibonacciIterator:
    def __init__(self, value):
        self.value = value
        self.current_num = 0
        self.next_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == 0:
            raise StopIteration
        current_value = self.current_num
        self.current_num, self.next_num = self.next_num, self.current_num + self.next_num
        self.value -= 1
        return current_value


if __name__ == '__main__':
    fibonacci_iter = FibonacciIterator(7)

    for number in fibonacci_iter:
        print(number)
