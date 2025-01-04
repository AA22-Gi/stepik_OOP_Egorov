"""
Класс FileReader

Ниже в коде представлена реализация класса FileReader,
который должен при итерации считывать построчно содержимое файла

Ваша задача - дописать метод __next__,
чтобы он возвращал по порядку строки из файла, пока содержимое файла не закончится.
Строку нужно очистить слева и справа от символов пробелов и переносов на новую строку
"""

class FileReader:
    def __init__(self, filename):
        self.file = open(filename, 'r')  # Открываем файл в режиме чтения
        self.current_line = None  # Переменная для хранения текущей строки

    def __iter__(self):
        return self

    def __next__(self):
        # Читаем следующую строку из файла
        self.current_line = self.file.readline()

        # Если достигнут конец файла, выбрасываем исключение StopIteration
        if not self.current_line:
            self.file.close()  # Закрываем файл
            raise StopIteration

        # Возвращаем очищенную строку
        return self.current_line.strip()  # Удаляем пробелы и переносы

for line in FileReader('lorem.txt'):
    print(line)