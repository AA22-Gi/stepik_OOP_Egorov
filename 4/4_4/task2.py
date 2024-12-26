"""
Создайте класс  Order, который имеет следующие методы:
    1)  метод __init__, который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя

    2)  магический метод __add__, который описывает добавление товара в список покупок.
        Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа
        и в конец добавляется новый товар. Покупатель в заказе остается прежним

    3)  магический метод __radd__, который описывает добавление товара в список покупок при правостороннем сложении.
        Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа
        и в начало списка покупок добавляется новый товар. Покупатель в заказе остается прежним

    4)  магический метод __sub__, который описывает исключение товара из списка покупок.
        Результатом вычитания должен быть новый заказ

    5)  магический метод __rsub__, который описывает исключение товара из списка покупок при правостороннем вычитании.
        Результатом должен быть таким же как и при __sub__
"""


class Order:
    def __init__(self, cart, customer):
        self.cart = cart  # Список покупок
        self.customer = customer  # Имя покупателя

    def __add__(self, item):
        # Создаем новый заказ с добавленным товаром в конец списка
        new_cart = self.cart + [item]
        return Order(new_cart, self.customer)

    def __radd__(self, item):
        # Создаем новый заказ с добавленным товаром в начало списка
        new_cart = [item] + self.cart
        return Order(new_cart, self.customer)

    def __sub__(self, item):
        # Создаем новый заказ без указанного товара
        new_cart = [i for i in self.cart if i != item]
        return Order(new_cart, self.customer)

    def __rsub__(self, item):
        # Создаем новый заказ без указанного товара
        return self.__sub__(item)

    def __repr__(self):
        return f"Order(customer='{self.customer}', cart={self.cart})"


if __name__ == '__main__':
    order = Order(['banana', 'apple'], 'Гена Букин')

    order_2 = order + 'orange'
    assert order.cart == ['banana', 'apple']
    assert order.customer == 'Гена Букин'
    assert order_2.cart == ['banana', 'apple', 'orange']

    order = 'mango' + order
    assert order.cart == ['mango', 'banana', 'apple']
    order = 'ice cream' + order
    assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

    order = order - 'banana'
    assert order.cart == ['ice cream', 'mango', 'apple']

    order3 = order - 'banana'
    assert order3.cart == ['ice cream', 'mango', 'apple']

    order = order - 'mango'
    assert order.cart == ['ice cream', 'apple']
    order = 'lime' - order
    assert order.cart == ['ice cream', 'apple']
    print('Good')