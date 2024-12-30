"""
Давайте вспомним задачу про формат дат

Одно из ее возможных решений выглядит так:
class DateEurope:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def format(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"


class DateUSA:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def format(self):
        return f"{self._month:02}/{self._day:02}/{self._year:04}"

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

На тот момент времени мы ничего не знали про наследование и из-за этого в коде возникло много дублирования.

Ваша задача переписать данный код при помощи наследования.
Для этого создайте базовый класс Date и вынесите в него все повторяющиеся фрагменты кода
"""


class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def format(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"


class DateEurope(Date):
    pass


class DateUSA(Date):

    def format(self):
        return f"{self._month:02}/{self._day:02}/{self._year:04}"


if __name__ == '__main__':
    print(issubclass(DateUSA, Date))
    print(issubclass(DateEurope, Date))
    print()

    d = DateEurope(5, 12, 2001)
    print(d.format())
    print(d.isoformat())
    print(isinstance(d, DateEurope))
    print(isinstance(d, Date))
    print()

    d = DateUSA(1, 5, 890)
    print(d.format())
    print(d.isoformat())
    print(isinstance(d, DateEurope))
    print(isinstance(d, Date))
    print(isinstance(d, DateUSA))
