"""
Сериализация класса - 2
Теперь давайте выполним сериализацию объектов, атрибутами которых могут быть другие объекты.
Для этого переделайте миксин JsonSerializableMixin, так чтобы он мог сериализовать такие объекты.

Внутри миксина JsonSerializableMixin обязательно должен быть метод to_json(),
который возвращает итоговую строку сериализации объекта. Все остальное вы можете создавать по своему усмотрению
"""
import json


class JsonSerializableMixin:
    def to_json(self):
        # Создаем словарь для сериализации
        result = {}

        # Получаем все атрибуты экземпляра
        for key, value in self.__dict__.items():
            # Если значение является экземпляром JsonSerializableMixin, вызываем его to_json()
            if isinstance(value, JsonSerializableMixin):
                result[key] = json.loads(value.to_json())
            # Если значение является списком, обрабатываем каждый элемент
            elif isinstance(value, list):
                result[key] = [json.loads(item.to_json()) if isinstance(item, JsonSerializableMixin)
                               else item for item in value]
            else:
                result[key] = value

        return json.dumps(result)


class Person(JsonSerializableMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(JsonSerializableMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(JsonSerializableMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_json() == '{"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}'

walter = Person("Walter White", 30, address)
walter.hobby = ['Chemistry', 'Cooking']
walter.is_danger = True

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
walter.company = Company("SCHOOL", company_address)
assert walter.to_json() == ('{"name": "Walter White", "age": 30, '
                            '"address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", '
                            '"zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, '
                            '"company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", '
                            '"city": "Albuquerque", "state": "NM", "zip_code": "12345"}}}')

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
walter.is_lucky = False

fring = Person("Gustavo Fring", 55,
               Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_json() == ('{"name": "Gustavo Fring", "age": 55, '
                           '"address": {"street": "Los Pollos Hermanos", '
                           '"city": "Albuquerque", "state": "NM", "zip_code": "12345"}, '
                           '"friends": [{"name": "Walter White", "age": 30, '
                           '"address": {"street": "123 Main St", "city": "Albuquerque", '
                           '"state": "NM", "zip_code": "987654"}, '
                           '"hobby": ["Chemistry", "Cooking"], "'
                           'is_danger": true, "company": {"name": "SCHOOL", "address": '
                           '{"street": "3828 Piermont Dr", "city": "Albuquerque", '
                           '"state": "NM", "zip_code": "12345"}}, "is_lucky": false}, '
                           '{"name": "Jesse Bruce Pinkman", "age": 27, '
                           '"address": {"street": "456 Oak St", "city": "Albuquerque", '
                           '"state": "NM", "zip_code": "12345"}}]}')
print('Good')
