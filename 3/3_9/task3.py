"""
Ваша задача - создать класс Date, который хранит информацию о дате: день, месяц и год.

Также класс Date должен иметь фабричный метод:
    from_str, который принимает строку в формате день-месяц-год
    и возвращает на ее основании вновь созданный экземпляр класса Date.

Проанализируйте входные данные тестовых значений для понимая состава атрибутов класса Date.

Для решения задания необходимо написать только реализацию класса Date.
"""


class Date:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def from_str(cls, date: str):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return cls(day, month, year)


    @property
    def day(self):
        return self._day


    @property
    def month(self):
        return self._month


    @property
    def year(self):
        return self._year


if __name__ == '__main__':
    day_1 = Date(20, 9, 1997)
    print(day_1.day)
    print(day_1.month)
    print(day_1.year)

    day_2 = Date(1, 2, 2003)
    print(day_2.day, day_2.month, day_2.year)
    print()

    day_1 = Date.from_str('12-4-2024')
    day_2 = Date.from_str('06-09-2022')
    print(day_1.day, day_1.month, day_1.year)
    print(day_2.day, day_2.month, day_2.year)
