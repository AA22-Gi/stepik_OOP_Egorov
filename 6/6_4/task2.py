"""
Напишите функцию sum_numbers, которая принимает один аргумент numbers.
Это должен быть список, состоящий из целых и вещественных чисел.
Функция sum_numbers должна возвращать сумму всех элементов списка,
но прежде чем находить сумму необходимо выполнить следующие проверки:

    1)  Аргумент numbers должен быть именно списком, если передан другой тип,
        необходимо выкинуть исключение TypeError('Аргумент numbers должен быть списком')

    2)  numbers не должен быть пустым, иначе возбуждаем исключение ValueError("Пустой список")

    3)  внутри numbers должны быть только типы int и float,
        иначе возбуждаем исключение TypeError('Неправильный тип элемента')
"""


def sum_numbers(numbers: list[int | float]) -> int | float:
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    elif len(numbers) == 0:
        raise ValueError("Пустой список")
    elif not all(isinstance(number, (int, float)) for number in numbers):
        raise TypeError('Неправильный тип элемента')
    else:
        return sum(numbers)


if __name__ == '__main__':
    for value in (True, (1, 2, 3), {1: 'hello'}, {1, 2, 3}):
        try:
            result = sum_numbers(value)
        except TypeError as error:
            print(error)

    try:
        result = sum_numbers([])
    except ValueError as error:
        print(error)

    try:
        sum_numbers([1, 'hello', 2, 3])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
    except TypeError as error:
        print(error)

    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0
