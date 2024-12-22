"""
Программист Терентий создал для ближайшей пиццерии класс Pizza
    class Pizza:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    который позволяет создавать пиццу с различными ингредиентами
        mozzarella = Pizza(['mozzarella', 'tomatoes'])
        pizza_ham = Pizza(['mozzarella', 'ham'])
        hawaii = Pizza(['mozzarella', 'tomatoes', 'pineapple', 'chicken'])
        print(mozzarella.ingredients)
        print(pizza)

    Но вскоре пиццерия поняла, что все гости заказывают только одни и те же виды пицц:
        - маргарита (состав: mozzarella, tomatoes);
        - пеперони (состав: mozzarella, peperoni, tomatoes);
        - барбекю (состав: mozzarella, red onion, sauce bbq, chicken);

    Им стало неудобно каждый раз при создании пиццы перечислять одни и те же ингредиенты,
    поэтому они попросили Терентия написать методы для создания каждого вида пиццы.

    Терентий убежал на пары, поэтому вы за него. Нужно создать следующие методы:
        1)  margherita
        2)  peperoni
        3)  barbecue

Каждый метод должен возвращать новую созданную пиццу соответствующего типа. Состав каждого вида пиццы указан выше.
Написать нужно только определение класса Pizza, сама реализация  методов на ваше усмотрение.
"""


class Pizza:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        ingredients = ['mozzarella', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def peperoni(cls):
        ingredients = ['mozzarella', 'peperoni', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def barbecue(cls):
        ingredients = ['mozzarella', 'red onion', 'sauce bbq', 'chicken']
        return cls(ingredients)


if __name__ == '__main__':
    bbq = Pizza.barbecue()
    peperoni = Pizza.peperoni()
    margherita = Pizza.margherita()
    print(sorted(bbq.ingredients))
    print(sorted(peperoni.ingredients))
    print(sorted(margherita.ingredients))
    print()

    margherita_1 = Pizza.margherita()
    margherita_2 = Pizza.margherita()
    print(sorted(margherita_1.ingredients))
    margherita_2.ingredients.append('ham')
    print(sorted(margherita_2.ingredients))
    print(sorted(margherita_1.ingredients))
    print()

    pizza = Pizza()
    bbq = pizza.barbecue()
    peperoni = pizza.peperoni()
    print(sorted(bbq.ingredients))
    print(sorted(peperoni.ingredients))
