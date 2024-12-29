"""
Создайте базовый класс Vehicle, у которого есть:
    1)  конструктор __init__, принимающий название транспортного средства, его максимальную скорость и пробег.
        Их необходимо сохранить в атрибуты экземпляра name, max_speed и mileage соответственно

    2)  метод display_info , который печатает информацию в следующем виде:
            Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}

Затем создайте подкласс Bus, унаследованный от Vehicle. Оставьте его пустым.
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')


class Bus(Vehicle):
    pass


if __name__ == '__main__':
    assert issubclass(Bus, Vehicle)
    bus_99 = Bus("Ikarus", 66, 124567)
    assert bus_99.name == 'Ikarus'
    assert bus_99.max_speed == 66
    assert bus_99.mileage == 124567
    bus_99.display_info()

    modelX = Vehicle('modelX', 240, 18)
    assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
    modelX.display_info()

    audi = Bus('audi', 123, 43)
    assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
    audi.display_info()
