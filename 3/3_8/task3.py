"""
Создайте класс Password, который имеет:

    1.метод __init__, который устанавливает значение атрибута password

    2.вычисляемое свойство strength, которое определяет стойкость пароля.
    Если длина пароля меньше 8 символов, то такой пароль считается слабым, свойство должно вернуть строку  "Weak".
    Сильным паролем считается тот, в котором длина символов 12 и более,
    в таком случае свойство возвращает строку "Strong". Во всех остальных случаях необходимо вернуть "Medium"
"""


class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return "Weak"
        elif len(self.password) > 12:
            return "Strong"
        else:
            return "Medium"


if __name__ == '__main__':
    pass
    pass_1 = Password("Alligator34")
    assert pass_1.password == "Alligator34"
    assert pass_1.strength == "Medium"
    assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

    pass_2 = Password("Alligator345678")
    assert pass_2.password == "Alligator345678"
    assert pass_2.strength == "Strong"
    pass_1.password = "123"
    assert pass_1.strength == "Weak"
    assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

    pass_3 = Password("345678")
    assert pass_3.strength == "Weak"
    print('Good')
    assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'
