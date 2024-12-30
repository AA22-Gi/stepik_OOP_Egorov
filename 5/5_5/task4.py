"""
Создайте базовый класс Vehicle, у которого есть:
    1)  метод __init__, принимающий название транспортного средства, пробег и вместимость.
        Их необходимо сохранить в атрибуты экземпляра name, mileage и capacity соответственно
    2)  метод fare, который возвращает стоимость проезда из расчета  capacity * 100
    3)  метод display, который печатает строку следующего вида: Total <name> fare is: <метод fare>

Затем создайте подкласс Bus, унаследованный от Vehicle. В нем необходимо:
    1)  переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег.
        Необходимо делегировать создание атрибутов name, mileage и capacity базовому классу,
        в качестве аргумента capacity  передайте значение 50
    2)  переопределить метод fare. Он должен получить стоимость проезда у родительского класса и увеличить ее на 10%.

После создайте подкласс Taxi, унаследованный от Vehicle. В нем необходимо:
    1)  переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег.
        Необходимо делегировать создание атрибутов name, mileage и capacity базовому классу,
        в качестве аргумента capacity передайте значение 4
    2)  переопределить метод fare. Он должен получить стоимость проезда у родительского класса и увеличить ее на 35%.
"""


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage):
        super().__init__(name, mileage, 50)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):
    def __init__(self, name, mileage):
        super().__init__(name, mileage, 4)

    def fare(self):
        return super().fare() * 1.35


if __name__ == '__main__':
    sc = Vehicle('Scooter', 100, 2)
    sc.display()

    merc = Bus("Mercedes", 120000)
    merc.display()

    polo = Taxi("Volkswagen Polo", 15000)
    polo.display()

    t = Taxi('x', 111)
    assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
    t.display()
    b = Bus('t', 123)
    assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
    b.display()
