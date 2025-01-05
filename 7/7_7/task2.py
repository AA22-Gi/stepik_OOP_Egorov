"""
На предыдущем шаге мы создали четыре класса StringValidation, IntValidation, FloatValidation и ListValidation.
Реализация всех перечисленных классов очень похожа друг на друга,
отличается только тип данных, на соответствие которому необходимо проверить.

Ваша задача - устранить дублирование кода путем создания класса TypeValidation,
который будет принимать тип данных, принадлежность к которому необходимо проверить.

Если проверка на переданный тип данных не проходит, необходимо выкидывать исключение ValueError с текстом

В атрибут <имя атрибута> можно сохранять только тип <тип данных>
В коде ниже представлена реализация класса Person, в которой используется дескриптор StringValidation.

Класс Person вам нельзя удалять, он используется для проверки.
Вам необходимо только добавить реализацию класса TypeValidation
"""


class TypeValidation:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.attribute_name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise ValueError(f'В атрибут {self.attribute_name} '
                             f'можно сохранять только тип {self.expected_type.__name__}')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)


class Person:
    age = TypeValidation(int)
    height = TypeValidation(float)
    name = TypeValidation(str)
    hobbies = TypeValidation(list)


if __name__ == '__main__':
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

    mike = Person()
    try:
        mike.name = 100
    except ValueError as e:
        print(e)
    try:
        mike.height = (1, 2, 3)
    except ValueError as e:
        print(e)
