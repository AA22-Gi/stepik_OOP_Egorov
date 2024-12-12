"""
Создайте класс Student, у которого есть:

    1) метод __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;

    2) приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
        Имя: <name>
        Возраст: <age>
        Направление: <branch>

    3) метод access_private_method, который вызывает приватный метод __display_details.
"""


class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}', f'Возраст: {self.__age}', f'Направление: {self.__branch}', sep='\n')

    def access_private_method(self):
        self.__display_details()


if __name__ == '__main__':
    piter = Student("Piter Parker", 34, "Information Security")
    piter.access_private_method()
    print(piter._Student__branch)
    print(piter._Student__name)
    print(piter._Student__age)
    piter._Student__display_details()
