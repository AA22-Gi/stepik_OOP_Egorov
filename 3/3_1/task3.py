"""
Создайте класс Constructor, в котором реализованы:

    Метод add_atribute, принимающий на вход название атрибута в виде строки и его значение.
    Задача метода add_atribute  — создать или изменить атрибут экземпляра по переданному имени атрибута;

    Метод display,  печатающий на экран словарь __dict__ у экземпляра.
Необходимо написать только определение класса Constructor
"""


class Constructor:
    def add_atribute(self, name: str, value):
        setattr(self, name, value)

    def display(self):
        print(self.__dict__)


if __name__ == '__main__':
    obj1 = Constructor()
    obj1.display()
    obj1.add_atribute('color', 'red')
    obj1.add_atribute('width', 20)
    obj1.display()
