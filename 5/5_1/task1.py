"""
Ваша задача создать следующие пустые классы:
    Vehicle
    Car
    Plane
    Boat
    RaceCar

Класс Vehicle является базовым классом, от которого наследуются все остальные.
Необходимо написать только определение классов
"""


class Vehicle:
    pass


class Car(Vehicle):
    pass


class RaceCar(Car):
    pass


class Plane(Vehicle):
    pass


class Boat(Vehicle):
    pass


if __name__ == '__main__':
    # Ниже располагается код для проверки
    vehicle = Vehicle()
    car = Car()
    plane = Plane()
    boat = Boat()
    race_car = RaceCar()

    assert isinstance(vehicle, Vehicle)
    assert isinstance(car, Car)
    assert isinstance(plane, Plane)
    assert isinstance(boat, Boat)
    assert isinstance(race_car, RaceCar)
    assert vehicle.__dict__ == {}
    assert car.__dict__ == {}

    assert issubclass(Car, Vehicle), "Класс Car должен наследоваться от Venicle"
    assert issubclass(Plane, Vehicle), "Класс Plane должен наследоваться от Venicle"
    assert issubclass(Boat, Vehicle), "Класс Boat должен наследоваться от Venicle"
    assert issubclass(RaceCar, Car), "Класс RaceCar должен наследоваться от Venicle"
    assert issubclass(RaceCar, Vehicle), "Класс RaceCar должен наследоваться от Venicle"
    print('Good')
