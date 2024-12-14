"""
Создайте класс Notebook, у которого есть:

    1.конструктор __init__, принимающий список записей, в нем могут находиться любые значения.
      Необходимо сохранить его в защищенном атрибуте ._notes

    2.свойство notes_list, которое распечатает содержимое атрибута ._notes
      в виде пронумерованного списка дел (см. пример ниже)
        note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
        note.notes_list

      После этого на экране вы должны увидеть:
        1.Buy Potato
        2.Buy Carrot
        3.Wash car
"""


class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for index, value in enumerate(self._notes, 1):
            print(f'{index}.{value}')


if __name__ == '__main__':
    note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
    note.notes_list
    print()

    note = Notebook(list(range(10, 20)))
    note.notes_list
    try:
        note.notes_list = [3, 4, 3]  # при попытке сохранить новое значение должна быть ошибка
    except AttributeError:
        pass