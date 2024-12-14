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
        self.dollars = dollars
        self.cents = cents
        self.total_cents = self.dollars * 100 + self.cents

    @property
    def dollars(self):
        return self.total_cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars > 0:
            self.dollars = dollars * 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.cents

    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 < new_cents < 100:
            self.total_cents = self.dollars * 100 + new_cents
        else:
            print('Error cents')
