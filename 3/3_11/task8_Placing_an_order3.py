"""
Задача «Оформление заказа» Часть 2

Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

    1)  метод __init__, принимающий на вход логин пользователя
        и необязательный аргумент — баланс его счета (по умолчанию 0).
        Логин необходимо сохранить в атрибуте login,
        а баланс необходимо присвоить сеттеру balance (см. пункт 4)

    2)  метод __str__, возвращающий строку вида:
            Пользователь {login}, баланс - {balance}

    3)  Свойство геттер balance, которое возвращает значение self.__balance

    4)  Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance

    5)  метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance

    6)  метод is_money_enough, который принимает числовое значение и проверяет,
        имеется ли у пользователя такая сумма на балансе.
        Данный метод должен возвращать булево значение:
        если такая сумма есть – True, если нет – False

    7)  метод payment  принимает числовое значение, которое должно списаться с баланса пользователя.
        Если на счете у пользователя не хватает средств, то необходимо вывести фразу:
            Не хватает средств на балансе. Пополните счет
        и отказ в платеже. Если средств хватает, списываем с баланса у пользователя указанную сумму.
        (Постарайтесь внутри реализации воспользоваться методом is_money_enough)

Необходимо только написать определение класса User
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login: str, balance: [int, float] = 0):
        self.login = login
        self.balance = balance

    def __str__(self) -> str:
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self) -> None:
        return self.__balance

    @balance.setter
    def balance(self, new_balance: [int, float]) -> None:
        self.__balance = new_balance

    def deposit(self, num: [int, float]) -> None:
        self.__balance += num

    def is_money_enough(self, num: [int, float]) -> bool:
        return num <= self.balance

    def payment(self, num: [int, float]):
        if self.is_money_enough(num):
            self.__balance -= num
        else:
            print(f'Не хватает средств на балансе. Пополните счет')


if __name__ == '__main__':
    billy = User('billy@rambler.ru')
    assert billy.__str__() == 'Пользователь billy@rambler.ru, баланс - 0'
    assert billy.is_money_enough(350) == False
    billy.deposit(100)
    billy.deposit(300)
    assert billy.is_money_enough(350) == True
    assert billy.__str__() == 'Пользователь billy@rambler.ru, баланс - 400'

    # Проверяем, что баланс не изменился после неудачного платежа
    initial_balance = billy.balance
    billy.payment(500)
    assert billy.balance == initial_balance  # Баланс должен остаться прежним

    billy.payment(150)
    assert billy.__str__() == 'Пользователь billy@rambler.ru, баланс - 250'
    print()

    jack = User('jack@gmail.ru', 800)
    assert jack.__str__() == 'Пользователь jack@gmail.ru, баланс - 800'
    assert jack.balance == 800
    jack.payment(600)
    jack.payment(200)

    # Проверяем, что баланс не изменился после неудачного платежа
    initial_balance_jack = jack.balance
    jack.payment(1)
    assert jack.balance == initial_balance_jack  # Баланс должен остаться прежним

    jack.balance = 1
    assert jack.payment(1) is None  # Проверяем, что платеж прошел
    assert jack.__str__() == 'Пользователь jack@gmail.ru, баланс - 0'
    print('Good')
