"""
Создайте класс BankAccount, который имеет:

    1)  атрибут класса bank_name со значением "Tinkoff Bank"

    2)  атрибут класса address со значением  "Москва, ул. 2-я Хуторская, д. 38А"

    3)  метод __init__, который устанавливает значения атрибутов name и balance : владелец счета и значение счета

    4)  класс метод create_account,
        который возвращает новый экземпляр класса BankAccount. Метод принимает имя клиента и сумму взноса

    5)  класс метод bank_info, который возвращает информацию о банке в виде:
        «{bank_name} is located in {address}»
"""


class BankAccount:
    bank_name = 'Tinkoff Bank'
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, summa):
        return cls(name, summa)

    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'


if __name__ == '__main__':
    oleg = BankAccount.create_account("Олег Тинкофф", 1000)
    assert isinstance(oleg, BankAccount)
    assert oleg.name == 'Олег Тинкофф'
    assert oleg.balance == 1000
    assert BankAccount.bank_info() == 'Tinkoff Bank is located in Москва, ул. 2-я Хуторская, д. 38А'

    ivan = BankAccount.create_account("Ivan Reon", 50)
    assert isinstance(ivan, BankAccount)
    assert ivan.name == 'Ivan Reon'
    assert ivan.balance == 50
    print('Good')
