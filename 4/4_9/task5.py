"""
Нам необходимо создать класс Building.

Мы должны научиться создавать здание определенной этажности и уметь бронировать за компанией определенный этаж в здании.
Важно, что в нашем классе за одним этажом может быть закреплена только одна компания.
Для этого в классе Building должны быть реализованы:
    1)  метод __init__, который принимает количество этажей в здании;

    2)  метод __setitem__, который закрепляет за определенным этажом компанию.
        Если этаж был занят другой компанией, нужно заменить название другой компанией;

    3)  метод __getitem__, который возвращает название компании с этого этажа.
        В случае, если этаж пустует, следует вернуть None;

    4)  метод __delitem__, который высвобождает этаж.

В этом задании вы сами решаете какие атрибуты создавать внутри класса,
главное реализовать магические методы из списка выше.
"""


class Building:
    def __init__(self, number_floors: int):
        self.number_floors = number_floors
        self.dict_company = dict()
        for i in range(1, number_floors + 1):
            self.dict_company[i] = None

    def __setitem__(self, key: int, value: str):
        if key <= self.number_floors:
            self.dict_company[key] = value

    def __getitem__(self, item):
        return self.dict_company[item]

    def __delitem__(self, key):
        self.dict_company[key] = None


if __name__ == '__main__':
    iron_building = Building(22)  # Создаем здание с 22 этажами
    iron_building[0] = 'Reception'
    iron_building[1] = 'Oscorp Industries'
    iron_building[2] = 'Stark Industries'
    print(iron_building[2])
    del iron_building[2]
    print(iron_building[2])