"""
В этой задаче мы напишем приложение, помогающее определить уровень доступа пользователя к запрашиваемому ресурсу.
В операционных системах выдаются права доступа к каждому ресурсу: файлу или каталогу.
Если у пользователя в списке его ролей присутствует та, которой разрешено взаимодействовать с файлом или каталогом,
то доступ к ресурсу будет разрешен. Вот так примерно работает система контроля доступа.
Давайте напишем ее простой аналог при помощи двух классов User и Access.

Создайте базовый класс User, у которого есть:

    1)  метод __init__, принимающий имя пользователя и его роль.
        Их необходимо сохранить в атрибуты экземпляра name и role соответственно.

Затем создайте класс Access, у которого есть:

    1)  приватный атрибут класса __access_list, в котором хранится список ['admin', 'developer']

    2)  приватный статик-метод __check_access,
        который принимает название роли и возвращает True, если роль находится в списке __access_list, иначе — False

    3)  публичный статик-метод get_access, который должен принимать экземпляр класса User и проверять,
        есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access.
        Если у пользователя достаточно прав, выведите на экран сообщение «User <name>: success»,
        если прав недостаточно — «AccessDenied».
        Если передается тип данных, отличный от экземпляра класса User, необходимо вывести сообщение: «AccessTypeError».

user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"
zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied
Access.get_access(5) # печатает AccessTypeError
"""


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role) -> bool:
        return role in Access.__access_list

    @staticmethod
    def get_access(instance):
        if not isinstance(instance, User):
            print('AccessTypeError')
        elif Access.__check_access(instance.role):
            print(f'User {instance.name}: success')
        else:
            print('AccessDenied')


if __name__ == '__main__':
    user1 = User('batya99', 'admin')
    Access.get_access(user1)  # печатает "User batya99: success"
    zaya = User('milaya_zaya999', 'user')
    Access.get_access(zaya)  # печатает AccessDenied
    Access.get_access(5)  # печатает AccessTypeError
