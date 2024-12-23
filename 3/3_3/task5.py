"""
Создайте класс Worker, у которого есть:

    метод __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт.
    Необходимо сохранить их в следующих атрибутах: name, salary, gender и passport.

    метод get_info, который распечатает информацию о сотруднике в следующем виде:
    «Worker {name}; passport-{passport}»

Пример использования класса Worker
    bob = Worker('Bob Moore', 330000, 'M', '1635777202')
    bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"

Ниже имеется список кортежей persons, содержащий информацию о десяти работниках.
На основании этих данных необходимо создать 10 экземпляров класса Worker и добавить их в список  worker_objects.
Работников в списке следует разместить в том же порядке, в каком они встречаются в списке persons.

В этом же порядке для каждого объекта в списке worker_objects вызовите метод get_info
"""


class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        return f'Worker {self.name}; passport-{self.passport}'


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

worker_objects = []

for person in persons:
    worker_objects.append(Worker(*person))

if __name__ == '__main__':
    for worker in worker_objects:
        print(worker.get_info())
