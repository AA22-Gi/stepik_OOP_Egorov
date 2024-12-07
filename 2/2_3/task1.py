"""
Ниже определен пустой класс SuperHero.
Ваша задача — создать два ЭК и сохранить их в переменные batman и superman.

Для ЭК, хранящегося в переменной batman, необходимо создать:
    атрибут can_fly с логическим значением False
    атрибут damage с числовым значением 175

Для ЭК, хранящегося в переменной superman, необходимо создать:
    атрибут can_fly с логическим значением True
    атрибут damage с числовым значением 285
    атрибут alter_ego со строковым значением «Кларк Кент»

Ничего выводить на экран в этом задании не требуется
"""


class SuperHero:
    pass


batman = SuperHero()
superman = SuperHero()

batman.can_fly = False
batman.damage = 175

superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'
