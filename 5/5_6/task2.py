"""
Вы создаете приложение для управления заметками и хотите добавить функционал аутентификации пользователей.

Для этого в этой задаче необходимо:
    1)  создать класс User, который принимает имя пользователя и пароль при инициализации,
        и имеет метод get_info(), который возвращает строку в виде:
            Имя пользователя: {self.username}

    2)  Создайте класс Authentication, состоящий из одного метода authenticate().
        Данный метод принимает имя пользователя и пароль, и возвращает True,
        если пользователь аутентифицирован успешно, и False, если аутентификация не удалась.

    3)  Создайте класс AuthenticatedUser, который наследуется от классов Authentication и User.
        Он не имеет своих методов и все поведение наследуют от родителей
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_info(self):
        return f'Имя пользователя: {self.username}'


class Authentication:
    def authenticate(self, username, password):
        return getattr(self, "username") == username and getattr(self, "password") == password


class AuthenticatedUser(Authentication, User):
    pass


if __name__ == '__main__':
    assert issubclass(AuthenticatedUser, User) is True
    assert issubclass(AuthenticatedUser, Authentication) is True

    user1 = AuthenticatedUser('user1', 'password1')
    assert user1.get_info() == 'Имя пользователя: user1'
    assert user1.authenticate('user1', 'password2') is False
    assert user1.authenticate('user1', 'password1') is True

    ted = AuthenticatedUser('ted_lawyer', 'alligator3')
    print(ted.get_info())
