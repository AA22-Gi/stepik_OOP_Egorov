"""
Вы работаете над проектом управления устройствами в доме.
Вам нужно создать иерархию классов для различных типов устройств и реализовать методы для управления ими.
В качестве части проекта вам нужно использовать механизмы slots и property для определения и защиты атрибутов классов.

    1)  Создайте класс Device, который будет служить базовым классом для всех устройств в доме.
        Класс "Device" должен иметь "slots" для защищенных атрибутов "_name", "_location" и "_status"(по умолчанию ON).
        Для атрибута "_name" создайте свойство только для чтения,
        а для атрибутов "_location" и "_status" - свойства для чтения и записи.
        Добавьте метод "turn_on" для изменения статуса устройства на "ON"
        и метод "turn_off" для изменения статуса на "OFF".

    2)  Создайте класс Light, который будет наследоваться от класса "Device" и представлять устройства освещения.
        Для этого определите слоты для атрибутов "_brightness" и "_color".
        Для атрибута "_brightness" создайте свойство для чтения и записи, а для атрибута "_color" - только для чтения.

    3)  Создайте класс Thermostat, который будет наследоваться от класса "Device"
        и представлять устройства управления температурой.
        В классе Thermostat определите слоты для атрибутов "_current_temperature" и "_target_temperature".
        Оба атрибута должны управляться свойствами для чтения и записи.

    4)  Создайте класс SmartTV, который будет наследоваться от класса "Device"
        и представлять устройства для просмотра телевизионных каналов.
        В классе SmartTV определите слоты для атрибута "_channel".
        Создайте свойства для управления чтением и записью атрибута _channel.
"""


class Device:
    __slots__ = ("_name", "_location", "_status")

    def __init__(self, name, location, status="ON"):
        self._name = name
        self.location = location
        self.status = status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"


class Light(Device):
    __slots__ = ("_brightness", "_color")

    def __init__(self, name, location, brightness, color, status="ON"):
        super().__init__(name, location, status)
        self.brightness = brightness
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value

    @property
    def color(self):
        return self._color


class Thermostat(Device):
    __slots__ = ("_current_temperature", "_target_temperature")

    def __init__(self, name, location, current_temperature, target_temperature, status="ON"):
        super().__init__(name, location, status)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value


class SmartTV(Device):
    __slots__ = ("_channel",)

    def __init__(self, name, location, channel, status="ON"):
        super().__init__(name, location, status)
        self.channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


if __name__ == '__main__':
    device1 = Device('Устройство 1', 'Гостиная')
    assert device1.name == 'Устройство 1'
    assert device1._name == 'Устройство 1'
    assert device1.location == 'Гостиная'
    assert device1._location == 'Гостиная'
    assert device1.status == 'ON'
    assert device1._status == 'ON'

    device1.turn_off()
    assert device1.status == 'OFF'
    device1.location = 'Кухня'
    assert device1.location == 'Кухня'
    assert device1._location == 'Кухня'
    device1.turn_on()
    assert device1.status == 'ON'

    light1 = Light('Лампа', 'Гостиная', 50, 'белый')
    light1.name == 'Лампа'
    light1.location == 'Гостиная'
    light1.status == 'ON'
    light1.brightness == '50'
    light1.color == 'белый'

    light1.turn_off()
    light1.status == 'OFF'

    thermostat_1 = Thermostat('Термометр', 'Балкон', 10, 15)
    thermostat_1.name == 'Термометр'
    thermostat_1.location == 'Балкон'
    thermostat_1.status == 'ON'
    thermostat_1.current_temperature == 10
    thermostat_1.target_temperature == 15

    tv = SmartTV('Samsung', 'Спальня', 20)
    tv.name == 'Термометр'
    tv.location == 'Балкон'
    tv.status == 'ON'
    tv.channel == 20

    print('GOOD')
