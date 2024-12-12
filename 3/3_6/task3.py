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

