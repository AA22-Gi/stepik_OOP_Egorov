"""
Создайте класс UserMail, у которого есть:

    1.метод __init__, принимающий 2 аргумента: логин и почтовый адрес.
      Их необходимо сохранить в экземпляр как атрибуты login и __email (обратите внимание, приватный атрибут).

    2.метод-геттер get_email, который возвращает приватный атрибут __email.

    3.метод-сеттер set_email, который принимает в виде строки новую почту.
      Метод должен проверять, что в новой почте есть только один символ @ и после него есть точка.
      Если данные условия выполняются, новая почта сохраняется в атрибут __email,
      в противном случае выкидывайте исключение ValueError с сообщением «ErrorMail:<почта>».

    4.создайте свойство email, у которого геттером будет метод get_email, а сеттером  метод set_email.
"""


class UserMail:
    def __init__(self, login: str, email: str):
        self.login = login
        self.__email = None  # Инициализация приватного атрибута
        self.set_email(email)

    def get_email(self):
        return self.__email

    def set_email(self, new_email: str):
        if isinstance(new_email, str) and new_email.count('@') == 1:
            index_ = new_email.index('@')
            if '.' in new_email[index_:]:
                self.__email = new_email
            else:
                raise ValueError(f'ErrorMail:{new_email}')
        else:
            raise ValueError(f'ErrorMail:{new_email}')

    email = property(fget=get_email, fset=set_email)


if __name__ == '__main__':
    k = UserMail('belosnezhka', 'prince@wait.you')
    print(k.email)
    print(k.login)
    for value in [True, 'prince@still@.wait', 'prince@stillwait']:
        try:
            k.email = value
        except ValueError as e:
            print(e)

    k.email = 'prince@still.wait'
    print(k.get_email())
    try:
        k.email = 'pri.nce@stillwait'
    except ValueError as e:
        print(e)
    print(k.email)
