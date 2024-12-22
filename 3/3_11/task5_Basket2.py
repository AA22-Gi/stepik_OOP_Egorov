"""
С предыдущего урока у вас должен быть создан класс  File, у которого имеются:
    1)  метод __init__;
    2)  метод  restore_from_trash;
    3)  метод  remove;
    4)  метод read;
    5)  метод write.

Далее создайте класс  Trash, у которого есть:
    1)  атрибут класса  content, изначально равный пустому списку

    2)  статик-метод  add, который принимает файл и сохраняет его в корзину:
        для этого нужно добавить его в атрибут content и проставить файлу в атрибут in_trash значение True.
        Если в метод add передается не экземпляр класса File, необходимо вывести сообщение:
        В корзину можно добавлять только файл

    3)  статик-метод  clear, который запускает процесс очистки файлов в корзине.
        Необходимо для всех файлов, хранящихся в атрибуте content,
        в порядке их добавления в корзину вызвать метод файла remove.
        Атрибут content  после очистки должен стать пустым списком.
        Сама процедура очистки должна начинаться фразой:
        Очищаем корзину и заканчиваться фразой Корзина пуста

    4)  статик-метод  restore, который запускает процесс восстановления файлов из корзины.
        Необходимо для всех файлов, хранящихся в атрибуте content,
        в порядке их добавления в корзину вызвать метод файла restore_from_trash.
        Атрибут content  после очистки должен стать пустым списком.
        Сама процедура восстановления должна начинаться фразой:
        Восстанавливаем файлы из корзины  и заканчиваться фразой  Корзина пуста
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


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print('В корзину можно добавлять только файл')
            return  # Возвращаемся, чтобы не добавлять не файл
        Trash.content.append(file)
        file.in_trash = True


    @staticmethod
    def clear():
        print('Очищаем корзину')
        for file in Trash.content:
            file.remove()
        Trash.content.clear()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content.clear()
        print('Корзина пуста')


if __name__ == '__main__':
    f1 = File('puppies.jpg')
    f2 = File('cat.jpg')
    f3 = File('xxx.doc')
    passwords = File('pass.txt')

    for file in [f1, f2, f3, passwords]:
        assert file.is_deleted is False
        assert file.in_trash is False

    f3.read()
    f3.remove()
    assert f3.is_deleted is True
    f3.read()
    f3.write('hello')

    assert Trash.content == []

    Trash.add(f2)
    Trash.add(passwords)
    Trash.add(f3)

    f1.read()
    Trash.add(f1)
    f1.read()

    for file in [f1, f2, f3, passwords]:
        assert file.in_trash is True

    for f in [f2, passwords, f3, f1]:
        assert f in Trash.content

    Trash.restore()
    assert Trash.content == [], 'После восстановления корзина должна была очиститься'

    Trash.add(passwords)
    Trash.add(f2)
    Trash.add('hello')
    Trash.add(f1)

    for f in [passwords, f2, f1]:
        assert f in Trash.content

    Trash.clear()

    for file in [passwords, f2, f1]:
        assert file.is_deleted is True

    assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

    f1.read()
