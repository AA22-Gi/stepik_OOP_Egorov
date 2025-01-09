"""
Создайте дата-класс  Location

В нем должны быть описаны следующие атрибуты

    name — обязательный, тип строка
    longitude — необязательный, вещественный тип, значение по умолчанию 0
    latitude  необязательный, вещественный тип, значение по умолчанию 11.5

Создайте ЭК Location со значениями name='Stonehenge', longitude=51, latitude=1.5
и сохраните его в переменную stonehenge
"""
from dataclasses import dataclass


@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5


stonehenge = Location('Stonehenge', longitude=51, latitude=1.5)
