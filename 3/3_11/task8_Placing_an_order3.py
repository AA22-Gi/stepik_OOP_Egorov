"""
Задача «Оформление заказа» Часть 3

Последний штрих — создание класса корзины, куда пользователь будет складывать товары.
Для этого нам понадобятся ранее созданные классы User и Product

Итак, создаем класс Cart, который содержит:

    1)  метод __init__, принимающий на вход экземпляр класса User.
        Его необходимо сохранить в атрибуте user.
        Помимо этого, метод  должен создать атрибут goods — пустой словарь (лучше использовать defaultdict).
        Он нужен будет для хранения товаров и их количества (ключ словаря — товар, значение — количество).
        И еще нам понадобится создать защищенный атрибут .__total со значением 0.
        В нем будет храниться итоговая сумма заказа

    2)  метод add принимает на вход экземпляр класса Product
        и необязательный аргумент — количество товаров (по умолчанию 1).
        Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара
        на переданное значение количества и пересчитать атрибут self.__total

    3)  метод remove принимает на вход экземпляр класса Product
        и необязательный аргумент — количество товаров (по умолчанию 1).
        Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара
        на переданное значение количества и пересчитать атрибут self.__total.
        Обратите внимание на то, что количество товара в корзине не может стать отрицательным, как и итоговая сумма;

    4)  свойство геттер total, которое возвращает значение self.__total;

    5)  метод order  должен использовать метод payment из класса User и передать в него итоговую сумму корзины.
        В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен»,
        в противном случае - «Проблема с оплатой»;

    6)  метод print_check, печатающий на экран чек. Он должен начинаться со строки
        ---Your check---
        Затем выводится состав корзины в алфавитном порядке по названию товара в виде
        {Имя товара} {Цена товара} {Количество товара} {Сумма}
        И заканчивается чек строкой
        ---Total: {self.total}---
"""
from collections import defaultdict


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


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = defaultdict(int)  # Словарь для хранения товаров и их количества
        self.__total = 0  # Итоговая сумма заказа

    def add(self, product: Product, count_goods: int = 1):
        self.goods[product] += count_goods
        self.__total += product.price * count_goods  # Увеличиваем итоговую сумму

    def remove(self, product: Product, count_goods: int = 1):
        if product in self.goods:
            current_count = self.goods[product]
            if current_count >= count_goods:
                self.goods[product] -= count_goods
                self.__total -= product.price * count_goods  # Уменьшаем итоговую сумму
                if self.goods[product] == 0:  # Удаляем товар, если его количество стало 0
                    del self.goods[product]
            else:
                del self.goods[product]
                self.__total -= product.price * current_count  # Уменьшаем итоговую сумму на все оставшиеся товары

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.is_money_enough(self.__total):
            self.user.payment(self.__total)
            print("Заказ оплачен")
        else:
            print(f'Не хватает средств на балансе. Пополните счет')
            print("Проблема с оплатой")

    def print_check(self):
        print('---Your check---')
        for product in sorted(self.goods.keys(), key=lambda p: p.name):  # Сортируем по имени товара
            quantity = self.goods[product]
            total_price = product.price * quantity
            print(f'{product.name} {product.price} {quantity} {total_price}')
        print(f'---Total: {self.total}---')


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

    billy = User('billy@rambler.ru')

    lemon = Product('lemon', 20)
    carrot = Product('carrot', 30)

    cart_billy = Cart(billy)
    print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
    cart_billy.add(lemon, 2)
    cart_billy.add(carrot)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Your check---
    carrot 30 1 30
    lemon 20 2 40
    ---Total: 70---'''
    cart_billy.add(lemon, 3)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Your check---
    carrot 30 1 30
    lemon 20 5 100
    ---Total: 130---'''
    cart_billy.remove(lemon, 6)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Your check---
    carrot 30 1 30
    ---Total: 30---'''
    print(cart_billy.total)  # 30
    cart_billy.add(lemon, 5)
    cart_billy.print_check()
    ''' Печатает текст ниже
    ---Your check---
    carrot 30 1 30
    lemon 20 5 100
    ---Total: 130---'''
    cart_billy.order()
    ''' Печатает текст ниже
    Не хватает средств на балансе. Пополните счет
    Проблема с оплатой'''
    cart_billy.user.deposit(150)
    cart_billy.order()  # Заказ оплачен
    print(cart_billy.user.balance)  # 20
