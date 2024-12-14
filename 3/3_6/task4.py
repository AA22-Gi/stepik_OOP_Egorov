"""
Предыдущая реализация класса UserMail проверяла при помощи свойства корректность электронного ящика пользователя,
но логин пользователя никаких проверок не проходил. Давайте это исправим

Логин хранился у нас в атрибуте login. Теперь под этим именем должно быть создано свойство login,
которое управляет установкой логина и получением значения логина.
Для атрибута придумайте другое название

Свойство login должно проверять переданный логин на уникальность:
в системе не должно находиться более одного пользователя с одинаковыми логинами в один момент времени.
Если пользователю пытаются в качестве логина сохранить не строковое значение,
необходимо вызвать исключение TypeError с сообщением «<значение> не является строкой».
Если в качестве логина хотят сохранить неуникальное название, то нужно вызвать исключение ValueError
с сообщением «Логин <значение> уже имеется в системе»

Ваша задача - дописать реализацию свойства login в класс UserMail. Все остальное - на ваше усмотрение
"""


class UserMail:
    logins_list = []

    def __init__(self, login: str, email: str):
        self.authorization = None
        self.set_login(login)
        self.__email = None  # Инициализация приватного атрибута
        self.set_email(email)

    def get_email(self):
        return self.__email

    def set_email(self, new_email: str):
        if (isinstance(new_email, str) and
                new_email.count('@') == 1 and
                '.' in new_email[new_email.index('@'):]):
            self.__email = new_email
        else:
            raise ValueError(f'ErrorMail: {new_email}')

    def get_login(self):
        return self.authorization

    def set_login(self, login: str):
        if login in UserMail.logins_list:
            raise ValueError(f'Логин {login} уже имеется в системе')
        if not isinstance(login, str):
            raise TypeError(f'{login} не является строкой')
        if self.authorization is not None:
            UserMail.logins_list.remove(self.authorization)
        UserMail.logins_list.append(login)
        self.authorization = login

    email = property(fget=get_email, fset=set_email)
    login = property(fget=get_login, fset=set_login)


if __name__ == '__main__':
    users = [
        UserMail("person", 'hello@com.org'),
        UserMail("person1", 'hello1@com.org'),
        UserMail("person2", 'hello2@com.org'),
    ]

    try:
        UserMail("person1", 'hello3@com.org')
    except ValueError as e:
        print(e)

    try:
        UserMail("person2", 'hello4@com.org')
    except ValueError as e:
        print(e)

    r = UserMail("person3", 'hello5@com.org')
    print(r.login)
