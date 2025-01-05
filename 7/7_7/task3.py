"""
Давайте вернемся к нашей реализации класса StringValidation, вот как она выглядела:
class StringValidation:

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)

В разделе изучения теории по методу __set_name__ мы реализовали класс StringValidation.

Ваша задача - добавить дополнительную валидацию на минимальную длину строки.
Само значение минимально допустимого предела будет передаваться в дескриптор при инициализации.
Если проверка на минимальную длину не проходит, необходимо выкинуть исключение ValueError с текстом:
    Длина атрибута <название атрибута> должна быть не меньше <минимальный лимит> символов
"""


class StringValidation:
    def __init__(self, value: int):
        self.len_value = value

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        if len(value) < self.len_value:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна быть не меньше {self.len_value} символов')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)


if __name__ == '__main__':
    class Person:
        name = StringValidation(5)
        last_name = StringValidation(7)


    p = Person()
    p.name = 'Michail'
    p.last_name = 'Lermontov'
    print(p.name, p.last_name)
    print()


    class Person:
        name = StringValidation(3)
        last_name = StringValidation(9)


    p = Person()
    try:
        p.name = 'M.'
    except ValueError as ex:
        print(ex)
    p.name = 'Misha'
    try:
        p.last_name = 'Sechin'
    except ValueError as ex:
        print(ex)
    p.last_name = 'Lermontov'
    print(p.name, p.last_name)
