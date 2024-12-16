"""
Хозяева пиццерии хотят иметь возможность быстро рассчитывать стоимость отдельного ингредиента
и полную стоимость пиццы.  Для это вам необходимо в классах  Pizza и Ingredient
создать вычисляемое свойство cost, которое вернет стоимость по следующему правилу:

    1)  для класса Ingredient надо посчитать стоимость исходя из массы ингредиента
        и стоимости ингредиента, указанной за 100 грамм (атрибут экземпляра price);

    2)  для класса Pizza  стоимость определяется суммарной стоимостью всех ингредиентов
        плюс 100 рублей за основу пиццы из теста.

Начальная реализация классов Pizza и Ingredient уже имеется, необходимо дописать вычисляемое свойство cost.
"""
from importlib.metadata import pass_none


class Ingredient:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price  # стоимость за 100гр

    @property
    def cost(self):
        return self.weight / 100 * self.price


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    @property
    def cost(self):
        res = 100
        for ingredient in self.ingredients:
            res += ingredient.cost
        return res


if __name__ == '__main__':
    chicken = Ingredient('chicken', 200, 80)
    mozzarella = Ingredient('mozzarella', 300, 110)
    sauce_bbq = Ingredient('sauce bbq', 150, 70)
    red_onion = Ingredient('red onion', 150, 50)

    print('Цена курицы', chicken.cost)
    print('Цена моцарелы', mozzarella.cost)
    print('Цена соуса', sauce_bbq.cost)
    print('Цена красного лука', red_onion.cost)

    barbecue = Pizza('BBQ', [chicken, mozzarella, sauce_bbq, red_onion])
    print('Стоимость пиццы BBQ', barbecue.cost)
    print()

    tomatoes = Ingredient('tomatoes', 200, 170)
    cheese = Ingredient('mozzarella', 400, 150)
    peperoni = Ingredient('peperoni', 300, 120)
    print('Цена помидор', tomatoes.cost)
    print('Цена сыра', cheese.cost)
    print('Цена колбасы', peperoni.cost)

    peperoni_pizza = Pizza('Пеперони')
    peperoni_pizza.ingredients.append(tomatoes)
    peperoni_pizza.ingredients.append(cheese)
    peperoni_pizza.ingredients.append(peperoni)
    print('Стоимость пиццы пеперони', peperoni_pizza.cost)
