"""
В этой задаче мы будем создавать базовый класс PrettyPrint,
задача которого красиво вывести экземпляр любого дочернего класса.
Формат вывода должен быть следующим:
    НазваниеКласса(атрибут1=ЗначениеАтрибута1, атрибут2=ЗначениеАтрибута2, ....)

Класс PrettyPrint должен сперва распечатать название класса экземпляра и затем в скобках
вывести все его атрибуты и значения. Между атрибутами должны стоять запятая с пробелом.
Выводить атрибуты нужно в том же порядке, в котором они находятся в словаре __dict__

Если у дочернего класса есть реализация метода __str__, то отрабатывать должен именно он,
а не метод __str__ класса  PrettyPrint
"""


class PrettyPrint:

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{class_name}({attributes})"


if __name__ == '__main__':
    class Person(PrettyPrint):
        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age


    artem = Person('Artem', 'Egorov', 33)
    ivan = Person('Ivan', 'Ivanov', 45)
    print(artem)
    print(ivan)
    print()


    class Student(PrettyPrint):
        def __init__(self, name, surname, student_id, faculty, specialty):
            self.student_id = student_id
            self.name = name
            self.surname = surname
            self.faculty = faculty
            self.specialty = specialty


    student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
    student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
    print(student_1)
    print(student_2)
    print()


    class Student(PrettyPrint):
        def __init__(self, name, surname, student_id, faculty, specialty):
            self.student_id = student_id
            self.name = name
            self.surname = surname
            self.faculty = faculty
            self.specialty = specialty

        def __str__(self):
            return f"{self.name} {self.surname}"


    student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
    student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
    print(student_1)
    print(student_2)
    print()


    class Person(PrettyPrint):
        pass


    p = Person()
    print(p)
