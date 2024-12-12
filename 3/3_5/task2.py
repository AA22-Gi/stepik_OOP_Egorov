"""
Создайте класс BankDeposit, который имеет следующие методы:

    1) метод __init__, который устанавливает значения атрибутов name, balance и rate:
       владелец депозита, значение депозита и годовая процентная ставка.

    2) приватный метод __calculate_profit, который возвращает количество денег,
       которое заработает владелец счета через год с учетом его годовой ставки.

    3) публичный метод get_balance_with_profit, который возвращает общее количество средств,
       которое будет у владельца депозита через год.
"""


class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * self.rate / 100

    def get_balance_with_profit(self):
        return self.balance + self.__calculate_profit()


if __name__ == '__main__':
    account_2 = BankDeposit("Sarah Connor", 200, 27)
    print(account_2.name)
    print(account_2.balance)
    print(account_2.rate)
    print(account_2._BankDeposit__calculate_profit())
    print(account_2.get_balance_with_profit())
