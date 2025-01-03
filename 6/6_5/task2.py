"""
Создайте класс BankAccount, который представляет банковский счет, у которого есть:

    1)  метод __init__, принимающий баланс (атрибут balance)

    2)  метод deposit для пополнения баланса.
        Если пользователь пытается внести отрицательную сумму на счет,
        должно возникать исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):

    3)  метод withdraw для вывода денег.
        Если пользователь пытается снять больше денег, чем есть на счете,
        должно возникать исключение InsufficientFundsError("Недостаточно средств для снятия")

Исключения NegativeDepositError и InsufficientFundsError вам также необходимо создать
"""


class NegativeDepositError(Exception): ...
class InsufficientFundsError(Exception): ...


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, add_money):
        if add_money < 0:
            raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
        self.balance += add_money

    def withdraw(self, sub_money):
        if self.balance < sub_money:
            raise InsufficientFundsError("Недостаточно средств для снятия")
        self.balance -= sub_money


if __name__ == '__main__':
    try:
        raise InsufficientFundsError("Недостаточно средств")
    except Exception as e:
        if not isinstance(e, InsufficientFundsError):
            raise ValueError('Реализуйте исключение InsufficientFundsError')

    try:
        raise NegativeDepositError("Внесено отрицательное значение")
    except Exception as e:
        if not isinstance(e, NegativeDepositError):
            raise ValueError('Реализуйте исключение NegativeDepositError')

    account = BankAccount(100)
    assert account.balance == 100

    account.deposit(50)
    assert account.balance == 150

    account.withdraw(75)
    assert account.balance == 75

    try:
        account.withdraw(100)
    except InsufficientFundsError as e:
        print(e)  # "Недостаточно средств"

    assert account.balance == 75

    try:
        account.deposit(-50)
    except NegativeDepositError as e:
        print(e)  # "Внесено отрицательное значение"
