"""
Создайте класс Celsius, который представляет температуру в градусах Цельсия.
Основная задача класса - предоставить возможность конвертировать температуру из градусов Цельсия в градусы Фаренгейта,
а также обеспечить контроль за корректностью введенных значений.

Класс Celsius, должен иметь:
    1.метод __init__, который принимает значение температуры в градусах по Цельсию и сохраняет в атрибут экземпляра.

    2.метод to_fahrenheit, который выполняет конвертацию температуры из градусов Цельсия в градусы Фаренгейта по формуле
        °F = (°C × 9/5) + 32  и возвращает результат этой конвертации

    3.свойство-геттер temperature, которое предоставляет доступ к значению температуры

    4.свойство-сеттер temperature, которое выполняется при установке нового значения температуры.
    Если значение меньше -273.15 градусов Цельсия (абсолютный ноль), вызывается исключение ValueError.
    В противном случае, происходит установка нового значения температуры.
"""


class Celsius:
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius

    def to_fahrenheit(self):
        return (self.temp_celsius * 9 / 5) + 32

    @property
    def temperature(self):
        return self.temp_celsius

    @temperature.setter
    def temperature(self, new_temp_celsius: [int, float]):
        if new_temp_celsius < -273.15:
            raise ValueError
        self.temp_celsius = new_temp_celsius


if __name__ == '__main__':
    celsius = Celsius(25)
    assert celsius.temperature == 25
    assert celsius.to_fahrenheit() == 77.0

    celsius.temperature = 30
    assert celsius.temperature == 30
    assert celsius.to_fahrenheit() == 86.0

    print('Good')
