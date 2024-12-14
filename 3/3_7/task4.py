"""
Создайте класс Money, у которого есть:

    1)  конструктор __init__, принимающий 2 аргумента: dollars, cents.
        По входным аргументам вам необходимо создать атрибут экземпляра total_cents.

    2)  свойство-геттер dollars, которое возвращает количество имеющихся долларов;

    3)  свойство-сеттер dollars, которое принимает целое неотрицательное число — количество долларов
        и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
        при этом значение центов должно сохраняться. В случае, если в сеттер передано число,
        не удовлетворяющее условию, нужно вывести на экран сообщение "Error dollars";

    4)  свойство геттер cents, которое возвращает количество имеющихся центов;

    5)  свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100
        количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
        при этом значение долларов должно сохраняться. В случае, если в сеттер передано число,
        не удовлетворяющее условию, нужно вывести на экран сообщение "Error cents";

    6)  метод __str__ (информация по данному методу), который возвращает строку вида
        "Ваше состояние составляет {dollars} долларов {cents} центов".
        Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами

В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
"""


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents


