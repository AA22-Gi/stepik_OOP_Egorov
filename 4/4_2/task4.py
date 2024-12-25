"""
Пицца
Теперь пиццерия хочет сделать красивое строковое представление для классов Pizza и Ingredient.
Представление класса Ingredient должно состоять из имени и количества грамм ингредиента.
Представление класса Pizza должно начинаться с фразы:
    Пицца <имя_пиццы> состоит из:
    и далее в отдельных строках должны быть перечислены все ингредиенты пиццы в порядке уменьшения количества грамм.
Начальная реализация классов Pizza и Ingredient уже имеется, необходимо дописать строковое представление.
"""


class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f'{self.name}: {self.weight}г.'


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def __str__(self) -> str:
        # Сортируем ингредиенты по весу в порядке убывания
        ingredients_list = sorted(self.ingredients, key=lambda x: x.weight, reverse=True)
        # Используем join для объединения строк
        ingredients_str = '\n'.join(str(ingredient) for ingredient in ingredients_list)
        return f'Пицца {self.name} состоит из:\n{ingredients_str}'



if __name__ == '__main__':
    barbecue = Pizza('BBQ', [
        Ingredient('chicken', 200),
        Ingredient('mozzarella', 300),
        Ingredient('sauce bbq', 150),
        Ingredient('red onion', 150)
    ])

    print(barbecue)
    print()

    tomatoes = Ingredient('tomatoes', 200)
    cheese = Ingredient('mozzarella', 400)
    print(tomatoes)
    print(cheese)

    peperoni = Pizza('Пеперони')
    peperoni.ingredients.append(tomatoes)
    peperoni.ingredients.append(cheese)
    print(peperoni)
