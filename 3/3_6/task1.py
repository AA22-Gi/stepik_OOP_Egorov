"""
Создайте класс BankAccount, который имеет следующие методы:

    1) метод __init__, который устанавливает значения атрибутов _account_number  и _balance: номер счета и баланс
    2) геттер-метод для атрибута _account_number
    3) геттер-метод для атрибута _balance
    4) сеттер-метод для атрибута _balance
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

