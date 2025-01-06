"""
Создайте дескриптор RangeValidator, который валидирует значение на принадлежность к определенному интервалу.
При инициализации класс RangeValidator получает значения начала и конца интервала.

При попытке сохранить нечисловое значение в дескриптор необходимо вызывать исключение:

TypeError('Неправильный тип данных')
При попытке сохранить значение в дескриптор, которое не принадлежит интервалу, необходимо вызвать исключение:

ValueError(f"Значение должно быть между <начало_интервала> и <конец_интервала>")
Ваша задача - только реализовать класс RangeValidator
"""
from idlelib.configdialog import is_int


class RangeValidator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_int(self, value) -> bool:
        return isinstance(value, int)

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.__name__, None)

    def __set__(self, instance, value):
        if not self.is_int(value):
            raise TypeError('Неправильный тип данных')
        if not (self.start <= value <= self.end):
            raise ValueError(f"Значение должно быть между {self.start} и {self.end}")
        instance.__dict__[self.__name__] = value


if __name__ == '__main__':
    class Temperature:
        celsius = RangeValidator(-273.15, 1000)


    temp = Temperature()
    try:
        temp.celsius = [1, 2]
    except TypeError as ex:
        print(ex)

    print()


    class Temperature:
        celsius = RangeValidator(-273.15, 1000)


    temp = Temperature()
    try:
        temp.celsius = -300
    except ValueError as ex:
        print(ex)
    print()


    class Temperature:
        celsius = RangeValidator(-273.15, 1000)
        kelvin = RangeValidator(0, 273)


    temp = Temperature()
    try:
        temp.celsius = -300
    except ValueError as ex:
        print(ex)
    try:
        temp.kelvin = 500
    except ValueError as ex:
        print(ex)
