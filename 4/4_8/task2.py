"""
Разные форматы
Вам необходимо создать класс DateUSA, в котором есть:
    1) метод __init__, принимающий 3 аргумента: день, месяц и год
    2) метод format, который возвращает строку в формате
        Месяц/День/Год

Также необходимо создать класс DateEurope, в котором есть:
    1) метод __init__, принимающий 3 аргумента: день, месяц и год.
    2) метод format, который возвращает строку в формате
        День/Месяц/Год

Также для двух классов необходимо реализовать метод isoformat, который должен возвращать строку в формате
        Год-месяц-день

Данный формат принят международной организацией по стандартизации для представления даты и времени.
Подробности можете почитать в интернете, ищите стандарт ISO 8601

Примечание: для отображения количества дней и месяцев необходимо отводить по два символа,
для года - четыре символа. Если символов не хватает, подставляйте незначащие нули
"""


class DateUSA:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self) -> str:
        return f'{self.month:02}/{self.day:02}/{self.year:04}'

    def isoformat(self):
        return f'{self.year:04}-{self.month:02}-{self.day:02}'


class DateEurope:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self) -> str:
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    def isoformat(self):
        return f'{self.year:04}-{self.month:02}-{self.day:02}'


if __name__ == '__main__':
    d = DateEurope(5, 12, 2001)
    print(d.format())
    print(d.isoformat())
    print()

    d = DateUSA(1, 5, 890)
    print(d.format())
    print(d.isoformat())
    print()

    dates = [
        DateUSA(1, 2, 2024),
        DateUSA(2, 2, 2024),
        DateEurope(20, 9, 2024),
        DateEurope(17, 12, 2024),
        DateUSA(3, 2, 2022),
        DateEurope(14, 3, 2001),
    ]
    for d in dates:
        print(d.format())
        print(d.isoformat())
        print('-' * 10)
