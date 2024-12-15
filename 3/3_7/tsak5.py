"""
В этом задании мы разработаем класс, позволяющий хранить информацию о часовом поясе.

Для этого вам необходимо создать класс TimeZone, который будет получать на вход название часового пояса,
смещение по часам относительно  всемирного координированного времени (UTC) и смещение по минутам относительно UTC.

Ваша задача создать три свойства для управления и контроля входящих значений. Их имена должны быть следующими:
    name, offset_hours, offset_minutes.

Свойство name должно позволять сохранять имя часового пояса только в виде непустой строки,
отбросив все незначимые пробелы. Если входное имя часового пояса не удовлетворяет этим требованиям,
выкидывайте исключение ValueError('Timezone bad name - <value>')

Свойство offset_hours должно позволять сохранять смещение по часам - допускаются
только целые числа от -12 до 14 включительно. Если входное смещение по часам не удовлетворяет этим требованиям,
выкидывайте исключение ValueError('Hour offset must be an integer.')
или ValueError('Offset must be between -12:00 and +14:00.') в зависимости от нарушения условия.

Свойство offset_minutes должно позволять сохранять смещение по минутам - допускаются только целые числа
от -59 до 59 включительно. Если входное смещение по минутам не удовлетворяет этим требованиям,
выкидывайте исключение ValueError('Minutes offset must be an integer.')
или ValueError('Minutes offset must between -59 and 59.') в зависимости от нарушения условия.

Остальная реализация атрибутов экземпляра и класса, а также и методов полностью на вашем усмотрении.
"""


class TimeZone:
    def __init__(self, name: str, offset_hours: int, offset_minutes: int):
        self.name = name  # Инициализация через сеттер
        self.offset_hours = offset_hours  # Инициализация через сеттер
        self.offset_minutes = offset_minutes  # Инициализация через сеттер

    @property
    def name(self):
        return self._name  # Защищённый атрибут

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str) or name.strip() == '':
            raise ValueError(f'Timezone bad name - {name}')
        else:
            self._name = name.strip()  # Инициализация защищённого атрибута

    @property
    def offset_hours(self):
        return self._offset_hours  # Защищённый атрибут

    @offset_hours.setter
    def offset_hours(self, offset_hours: int):
        if not isinstance(offset_hours, int):
            raise ValueError('Hour offset must be an integer.')
        elif offset_hours < - 12 or offset_hours > 14:
            raise ValueError('Offset must be between -12:00 and +14:00.')
        else:
            self._offset_hours = offset_hours  # Инициализация защищённого атрибута

    @property
    def offset_minutes(self):
        return self._offset_minutes  # Защищённый атрибут

    @offset_minutes.setter
    def offset_minutes(self, offset_minutes: int):
        if not isinstance(offset_minutes, int):
            raise ValueError('Minutes offset must be an integer.')
        elif offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59.')
        else:
            self._offset_minutes = offset_minutes  # Инициализация защищённого атрибута


if __name__ == '__main__':
    tz1 = TimeZone('ABC', -2, -15)
    print(tz1.name)
    print(tz1.offset_hours)
    print(tz1.offset_minutes)

    tz1.name = 'XYZ'
    tz1.offset_hours = 12
    tz1.offset_minutes = 0

    try:
        tz1.offset_hours = 67
    except ValueError as e:
        print(e)
    print(tz1.name, tz1.offset_hours, tz1.offset_minutes)
    print()

    # пустая строка не должна сохраняться
    for name in ['', None, '    ', 123, (1, 3), True]:
        try:
            TimeZone(name, 5, 34)
        except ValueError as e:
            print(e)
    print()

    try:
        TimeZone(' Abc ', -20.5, 34)
    except ValueError as e:
        print(e)

    try:
        TimeZone(' Abc ', -15, 34)
    except ValueError as e:
        print(e)

    try:
        TimeZone(' Abc ', 15, 34)
    except ValueError as e:
        print(e)

    tz = TimeZone(' Abc ', 10, 34)
    print(tz.name)
    print(tz.offset_hours)
    print(tz.offset_minutes)
