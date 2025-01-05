"""
В разделе изучения теории по методу __set_name__ мы реализовали класс StringValidation.

Ваша задача - по аналогии реализовать еще три класса: IntValidation, FloatValidation и ListValidation.

Каждый из них должен проверять перед установкой нового значения на принадлежность его к соответствующему типу данных.
Если значение не проходит проверку, выкидывайте исключение ValueError.
"""


class Validation:
    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)


class StringValidation(Validation):

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        instance.__dict__[self.attribute_name] = value


class IntValidation(Validation):

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError
        instance.__dict__[self.attribute_name] = value


class FloatValidation(Validation):

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError
        instance.__dict__[self.attribute_name] = value


class ListValidation(Validation):

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError
        instance.__dict__[self.attribute_name] = value


if __name__ == '__main__':
    class Person:
        age = IntValidation()
        height = FloatValidation()
        name = StringValidation()
        hobbies = ListValidation()


    mike = Person()
    mike.name = 'Mike'
    mike.age = 25
    mike.height = 1.80
    mike.hobbies = ['chess', 'gaming']
    print(mike.name)
    print(mike.age)
    print(mike.height)
    print(mike.hobbies)
    print()


    class Person:
        age = IntValidation()
        height = FloatValidation()
        name = StringValidation()
        hobbies = ListValidation()


    mike = Person()
    try:
        mike.name = 100
    except ValueError:
        print('В имя можно сохранить только строку')
    try:
        mike.height = (1, 2, 3)
    except ValueError:
        print('В значение веса можно сохранить только вещественное число')