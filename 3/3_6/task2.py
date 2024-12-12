"""
Создайте класс Employee, который имеет следующие методы:

    1) метод __init__, который устанавливает значения приватных атрибутов
       __name  и __salary: имя работника и его зарплату
    2) приватный геттер метод для атрибута __name
    3) приватный геттер метод для атрибута __salary
    4) приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут
       __salary только положительные числа. В остальных случаях не сохраняем переданное значение
       в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
    5) свойство title, у которого есть только геттер из пункта 2.
    6) свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.
"""


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, new_salary):
        if isinstance(new_salary, (int, float)) and new_salary > 0:
            self.__salary = new_salary
        else:
            print(f'ErrorValue:{new_salary}')

