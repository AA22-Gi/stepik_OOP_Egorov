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
    def __init__(self, name, offset_hours, offset_minutes):
        self.name = name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes
