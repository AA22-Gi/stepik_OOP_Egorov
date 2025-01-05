"""
Сперва четные индексы, потом все остальные

Усложним задачу про SequenceIterable
Теперь нужно создать итератор SequenceIterator,
который принимает контейнер данных в виде списка в момент инициализации и сохраняет его в атрибуте ЭК
    SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])

При итерации объект SequenceIterator должен  сперва выдать все элементы,
находящиеся на четных индексах (0, 2, 4 и т.д),
а затем элементы, имеющие нечетные индексы (1, 3, 5 и т.д.)

container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
# Печатает
1
4
43
hello
5
6
True
"""


class SequenceIterator:
    def __init__(self, value: list):
        even_list = [value[index] for index in range(len(value)) if index % 2 == 0]
        odd_list = [value[index] for index in range(len(value)) if index % 2 != 0]
        self.value = even_list + odd_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            raise StopIteration
        else:
            current_index = self.index
            self.index += 1
            return self.value[current_index]


if __name__ == '__main__':
    container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
    for i in container:
        print(i)
