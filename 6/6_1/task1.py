"""
Реализуйте класс Wallet, аналог денежного кошелька, содержащий информацию о валюте и остатке имеющихся средств на счете.
В данном классе должны быть реализованы:
    1)  метод __init__, который создает атрибуты currency и balance.
        Значения атрибутов currency и balance поступают при вызове метода __init__.
        При этом значение атрибута currency должно быть строкой, состоящей только из трех заглавных букв.
        Для этого необходимо сделать именно в такой последовательности следующие проверки:
            -   В случае, если передается не строка,
                нужно возбуждать исключение TypeError с текстом «Неверный тип валюты» ;
            -   В случае, если передается строка, длина которой не равна трем символам,
                нужно возбуждать исключение NameError с текстом «Неверная длина названия валюты»
            -   В случае, если строка не состоит из заглавных символов,
                нужно возбуждать исключение ValueError с текстом «Название должно состоять только из заглавных букв»

    2)  метод __eq__, для возможности сравнивания балансов кошельков.
        Операция сравнения доступна только для кошельков с одинаковой валютой.
        Если валюты различаются, необходимо возбудить исключение ValueError с текстом "Нельзя сравнить разные валюты".
        При попытке сравнить экземпляр класса Wallet с другими объектами
        необходимо возбудить исключение TypeError с текстом «Wallet не поддерживает сравнение с <объектом>»;

    3)  методы __add__ и __sub__ для возможности суммирования и вычитания кошельков.
        Складывать и вычитать мы можем только с другим экземпляром класса Wallet и только в случае,
        когда у них совпадает валюта (атрибуты currency).
        Результатом такого сложения должен быть новый экземпляр класса Wallet,
        у которого валюта совпадает с валютой операндов и значение баланса равно сумме/вычитанию их балансов
        (при вычитании баланс может оказаться отрицательным).
        Если попытаться сложить с объектом не являющимся экземпляром Wallet или значения валют у объектов не совпадают,
        необходимо возбудить исключение ValueError с текстом  «Данная операция запрещена»
"""


class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if not isinstance(value, str):
            raise TypeError('Неверный тип валюты')
        elif len(value) != 3:
            raise NameError('Неверная длина названия валюты')
        elif not value.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self._currency = value

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        else:
            return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        else:
            return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        else:
            return Wallet(self.currency, self.balance - other.balance)


if __name__ == '__main__':
    # Примеры использования и проверок
    wallet1 = Wallet('USD', 50)
    wallet2 = Wallet('RUB', 100)
    wallet3 = Wallet('RUB', 150)

    # Проверка на исключения
    try:
        wallet4 = Wallet(12, 150)
    except TypeError as e:
        assert str(e) == 'Неверный тип валюты'

    try:
        wallet5 = Wallet('qwerty', 150)
    except NameError as e:
        assert str(e) == 'Неверная длина названия валюты'

    try:
        wallet6 = Wallet('abc', 150)
    except ValueError as e:
        assert str(e) == 'Название должно состоять только из заглавных букв'

    # Проверки на равенство
    assert wallet2 != wallet3  # False
    assert wallet2 != wallet3  # True

    try:
        assert wallet2 == wallet1  # ValueError
    except ValueError as e:
        assert str(e) == 'Нельзя сравнить разные валюты'

    # Проверка сложения
    wallet7 = wallet2 + wallet3
    assert wallet7.currency == 'RUB'
    assert wallet7.balance == 250

    try:
        wallet2 + 45  # ValueError
    except ValueError as e:
        assert str(e) == 'Данная операция запрещена'

    print("Все проверки пройдены успешно!")
