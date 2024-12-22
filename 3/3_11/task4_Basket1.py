"""
Давайте реализуем ситуацию создания файлов и перемещения их в корзину. Задача будет состоять из двух частей
Часть 1

Создайте класс  File, у которого есть:

    1)  метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name.
        Также необходимо создать атрибуты in_trash, is_deleted  и записать в них значение False;

    2)  метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины»
        и проставляет в атрибут in_trash значение False;

    3)  метод  remove, который печатает фразу «Файл {name} был удален»
        и проставляет в атрибут is_deleted значение True;

    4)  метод read, который печатает:
            печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истинен, и выходит из метода;
            печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истинен, и выходит из метода;
            печатает фразу «Прочитали все содержимое файла {self.name}», если файл не удален и не в корзине;

    5)  метод write, который принимает значение content для записи и
            печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истинен, и выходит из метода;
            печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истинен, и выходит из метода;
            печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине.
"""


class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        if self.in_trash:
            print(f"Файл {self.name} восстановлен из корзины")
            self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")
            return
        if self.in_trash:
            print(f"ErrorReadFileTrashed({self.name})")
            return
        print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")
            return
        if self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")
            return
        print(f"Записали значение {content} в файл {self.name}")


if __name__ == '__main__':
    f1 = File('puppies.jpg')
    assert f1.name == 'puppies.jpg'
    assert f1.in_trash is False
    assert f1.is_deleted is False

    f1.read()  # Прочитали все содержимое файла puppies.jpg
    f1.remove()  # Файл puppies.jpg был удален
    assert f1.is_deleted is True
    f1.read()  # ErrorReadFileDeleted(puppies.jpg)

    passwords = File('pass.txt')
    assert passwords.name == 'pass.txt'
    assert passwords.in_trash is False
    assert passwords.is_deleted is False

    f3 = File('xxx.doc')

    assert f3.__dict__ == {'name': 'xxx.doc', 'in_trash': False, 'is_deleted': False}
    f3.read()
    f3.remove()
    assert f3.is_deleted is True
    f3.read()
    f3.in_trash = True
    f3.is_deleted = False
    f3.read()
    f3.write('hello')
    f3.restore_from_trash()
    assert f3.in_trash is False
    f3.write('hello')  # Записали значение «hello» в файл cat.jpg

    f2 = File('cat.jpg')
    f2.write('hello')  # Записали значение «hello» в файл cat.jpg
    f2.write([1, 2, 3])  # Записали значение «hello» в файл cat.jpg
    f2.remove()  # Файл cat.jpg был удален
    f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
