"""
В этой задаче у нас будет один родительский класс Transport и три дочерних класса: Car, Boat, Plane.

В классе Transport должны быть реализованы:
    1)  метод __init__, который создает атрибуты brand, max_speed и kind.
        Значения атрибутов brand, max_speed , kind поступают при вызове метода __init__.
        При этом значение kind не является обязательным и по умолчанию имеет значение None;

    2)  метод __str__, который будет возвращать строку формата:
        "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".

В классе Car должны быть реализованы:
    1)  метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue.
        Все значения этих атрибутов передаются при вызове класса Car.
        Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind родительскому классу Transport,
        при этом атрибуту kind передайте значение "Car";

    2)  свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина <gasoline_residue> л";

    3)  свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value,
        увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу
        'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'.
        Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.

В классе Boat должны быть реализованы:
    1)  метод __init__, принимающий три значения brand, max_speed, owners_name.
        Их нужно сохранить в соответствующие атрибуты. При этом внутри инициализации нужно делегировать
        создание атрибутов brand, max_speed , kind родительскому классу Transport,
        в атрибут kind при этом передайте значение "Boat";

    2)  метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.

В классе Plane должны быть реализованы:
    1)  метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity.
        Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport,
        при этом атрибуту kind передайте значение "Plane";

    2)  метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
"""


class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self) -> str:
        return f'Осталось бензина {self.__gasoline_residue} л'

    @gasoline.setter
    def gasoline(self, value: int) -> None:
        if not isinstance(value, int):
            print(f'Ошибка заправки автомобиля')
        else:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


if __name__ == '__main__':
    p1 = Transport('Chuck', 50)
    print(p1)
    assert isinstance(p1, Transport)
    assert p1.kind == None
    assert p1.brand == 'Chuck'
    assert p1.max_speed == 50
    assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}

    c1 = Car('RRR', 50, 150, 999)
    print(c1)

    assert isinstance(c1, Car)
    assert c1.kind == "Car"
    assert c1.brand == 'RRR'
    assert c1.max_speed == 50
    assert c1.mileage == 150
    assert c1.gasoline == 'Осталось бензина 999 л'
    c1.gasoline = 100
    assert c1.gasoline == 'Осталось бензина 1099 л'
    assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
                           'mileage': 150, '_Car__gasoline_residue': 1099}

    b1 = Boat('XXX', 1150, 'Arkasha')
    print(b1)
    assert isinstance(b1, Boat)
    assert b1.kind == "Boat"
    assert b1.brand == 'XXX'
    assert b1.max_speed == 1150
    assert b1.owners_name == 'Arkasha'

    pla = Plane('www', 2150, 777)
    print(pla)
    assert isinstance(pla, Plane)
    assert pla.kind == "Plane"
    assert pla.brand == 'www'
    assert pla.max_speed == 2150
    assert pla.capacity == 777

    transport = Transport('Telega', 10)
    print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
    bike = Transport('shkolnik', 20, 'bike')
    print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

    first_plane = Plane('Virgin Atlantic', 700, 450)
    print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
    first_car = Car('BMW', 230, 75000, 300)
    print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
    print(first_car.gasoline)  # Осталось бензина на 300 км
    first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
    print(first_car.gasoline)  # Осталось бензина на 350 км
    second_car = Car('Audi', 230, 70000, 130)
    second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
    first_boat = Boat('Yamaha', 40, 'Petr')
    print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
