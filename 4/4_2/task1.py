"""
Создайте класс Person, у которого есть:

    1)  конструктор __init__, принимающий 3 аргумента: name, surname, gender.
        Атрибут gender может принимать только 2 значения: «male» и «female», по умолчанию «male».
        Если в атрибут gender передается любое другое значение, печатать сообщение:
        «Не знаю, что вы имели в виду? Пусть это будет мальчик!»
        и проставить в атрибут gender значение «male»;

    2)  переопределить метод __str__ следующим образом:
            - если объект - мужчина (атрибут gender = «male»), возвращать строку «Гражданин <Фамилия> <Имя>»
            - если объект - женщина (атрибут gender = «female»), возвращать строку «Гражданка <Фамилия> <Имя>»
"""


class Person:
    def __init__(self, name: str, surname: str, gender: str = 'male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender == 'male':
            self.__gender = 'male'
        elif gender == 'female':
            self.__gender = gender
        else:
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self.__gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


if __name__ == '__main__':
    p = Person('Оби-Ван', 'Кеноби', True)
    print(p.name)
    print(p.surname)
    print(p.gender)
    print(p)
