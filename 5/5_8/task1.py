"""
По примеру из лекции создайте класс CountryPizza:
    - название «Деревенская пицца»
    - в составе должны быть помимо сыра еще ветчина, перец, оливки, пепперони, грибы и курица

Из перечисленных топпингов отсутствуют в коде ниже
    - ветчина(ham, стоимость 7)
    - перец (pepper, стоимость 3)
    - курица (chicken, стоимость 5)

Миксины для данных топпингов необходимо создать
Начинки добавляйте в пиццу в том же порядке, в котором они перечислены, чтобы вывод вашей программы совпал с тестом
"""


class BasePizza:
    BASE_PIZZA_PRICE = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        print("Adding pepperoni!")
        self.price += 5
        self.toppings += ['pepperoni']


class MushroomMixin:
    def add_mushrooms(self):
        print("Adding mushrooms!")
        self.price += 3
        self.toppings += ['mushrooms']


class OnionMixin:
    def add_onion(self):
        print("Adding onion!")
        self.price += 2
        self.toppings += ['onion']


class BaconMixin:
    def add_bacon(self):
        print("Adding bacon!")
        self.price += 6
        self.toppings += ['bacon']


class OlivesMixin:
    def add_olives(self):
        print("Adding olives!")
        self.price += 1
        self.toppings += ['olives']


class HamMixin:
    def add_ham(self):
        print("Adding ham!")
        self.price += 7
        self.toppings += ['ham']


class PepperMixin:
    def add_pepper(self):
        print("Adding pepper!")
        self.price += 3
        self.toppings += ['pepper']


class ChickenMixin:
    def add_chicken(self):
        print("Adding chicken!")
        self.price += 5
        self.toppings += ['chicken']


class OlivesPizza(BasePizza, OlivesMixin):
    def __init__(self):
        super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
        self.add_olives()


class PepperoniPizza(BasePizza, PepperoniMixin):
    def __init__(self):
        super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
        self.add_pepperoni()


class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):
    def __init__(self):
        super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_onion()
        self.add_bacon()


class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin, PepperoniMixin, MushroomMixin, ChickenMixin):
    def __init__(self):
        super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
        self.add_ham()
        self.add_pepper()
        self.add_olives()
        self.add_pepperoni()
        self.add_mushrooms()
        self.add_chicken()


# Создайте экземпляр CountryPizza в переменной pizza
pizza = CountryPizza()

# Код для проверки

assert pizza.name == 'Деревенская пицца'
assert pizza.price == 39
assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
print(pizza)
