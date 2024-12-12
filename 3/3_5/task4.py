"""
Создайте класс Employee, который имеет следующие методы:

    1) метод __init__, который устанавливает значения атрибутов name, __position, __hours_worked и __hourly_rate.

    2) приватный метод calculate_salary, который считает зарплату сотрудника,
       умножая отработанные часы на часовую оплату. Метод должен вернуть посчитанную зарплату.

    3) защищенный метод _set_position, который принимает название должности
       и изменяет пользователю значение атрибута __position.

    4) публичный метод get_position, который возвращает атрибут __position.

    5) публичный метод get_salary, который возвращает результат вызова приватного метода calculate_salary.

    6) публичный метод get_employee_details, который возвращает информацию о работнике в виде следующий строки
       "Name: {name}, Position: {position}, Salary: {salary}"
       Здесь значение salary должно рассчитываться при помощи приватного метода calculate_salary.
"""


class Employee:
    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate