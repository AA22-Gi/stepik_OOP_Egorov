"""
Перед вами класс BankAccount
    class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

Ваша задача дописать его таким образом, чтобы его экземпляры могли участвовать в операции сортировки списка,
в котором могут находиться только числа и другие экземпляры класса BankAccount
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        elif isinstance(other, (int, float)):
            return self.balance < other

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.balance > other

    @staticmethod
    def sort(values, reverse=False):
        values.sort(reverse=reverse)


if __name__ == '__main__':
    values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
    values.sort()
    print(*values)

    values = [
        BankAccount('Petrovich', 5),
        BankAccount('Ivan', 10),
        BankAccount('Andrey', 3),
        BankAccount('Lena', 15),
        BankAccount('Petr', 150)
    ]
    values.sort(reverse=True)
    print(*values)
