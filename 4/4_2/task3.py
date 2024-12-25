"""
Отображение товара.
Давайте определим магические методы __str__ и __repr__ для класса GroceryItem, представляющего продуктовый товар:

Создайте класс GroceryItem, который имеет следующие методы:
    1)  метод __init__, который устанавливает значения атрибутов name, price и quantity:
        название товара, его цену и количество

    2)  магический метод __str__, который возвращает строковое представление товара в следующем виде:
            Name: {name}
            Price: {price}
            Quantity: {quantity}

    3)  магический метод __repr__, который возвращает однозначное строковое представление объекта
            GroceryItem({name}, {price}, {quantity})
"""


class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return (f'Name: {self.name}\n'
                f'Price: {self.price}\n'
                f'Quantity: {self.quantity}')

    def __repr__(self) -> str:
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


if __name__ == '__main__':
    banana = GroceryItem('Banana', 10, 5)
    print(banana)
    print(f"{banana!r}")

    dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
    print(str(dragon_fruit))
    print(repr(dragon_fruit))
