"""
Создайте базовый класс Person, у которого есть:
    1)  метод __init__, принимающий имя и возраст человека.
        Их необходимо сохранить в атрибуты экземпляра name и age соответственно

    2)  метод display_person_info, который печатает информацию в следующем виде:
        Person: {name}, {age}

Затем создайте класс Company, у которого есть:
    1)  метод __init__, принимающий название компании и город ее основания.
        Их необходимо сохранить в атрибуты экземпляра company_name  и location соответственно

    2)  метод display_company_info, который печатает информацию в следующем виде:
        Company: {company_name}, {location}

И в конце создайте класс Employee, который:
    1)  унаследован от классов Person и Company

    2)  имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания.
        Необходимо делегировать создание атрибутов name и age  классу Person,
        а атрибуты company_name  и location должен создать класс Company
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)


if __name__ == '__main__':
    a = Person('Ivan', 32)
    a.display_person_info()

    a = Company('Zara', 'Prague')
    a.display_company_info()

    emp = Employee('Jessica', 28, 'Google', 'Atlanta')
    emp.display_person_info()
    emp.display_company_info()

    emp2 = Employee('Kolya', 11, 'Facebook', 'Seatle')
    emp2.display_person_info()
    emp2.display_company_info()
