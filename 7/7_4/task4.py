"""
Инвентаризация библиотеки

Представьте, что у библиотекаря имеется огромная коллекция книг.
В какую-то из этих книг он в далекой молодости положил 666 песо и теперь хочет их отыскать.
Его внук начал изучать python и познакомился с концепцией итератора.

Он предложил обойти все книги по порядку добавления их в библиотеку,
и затем для каждой отдельной книги обойти все ее страницы.
Но сам это реализовать не смог, просит помочь именно вас.

От внука вам досталась реализация классов Book и Library.
Класс Library делегирует реализацию итератора классу LibraryIterator
    def __iter__(self):
        return LibraryIterator(...)

Вот здесь у внука библиотекаря и возникла проблема.
Он не знает, что передавать в LibraryIterator и как организовать обход этой коллекции.
Помогите внучку, ведь ему еще математику делать на завтра.

Необходимо написать только реализацию класса LibraryIterator,
который обходит элементы библиотеки согласно примеру, расположенному в коде ниже.
Изучите код проверки класса LibraryIterator и ожидаемый вывод
"""


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self)  # передаем текущую библиотеку итератору


class LibraryIterator:
    def __init__(self, library):
        self.library = library
        self.book_index = 0
        self.page_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.book_index < len(self.library.books):
            book = self.library.books[self.book_index]
            if self.page_index < len(book.pages):
                page = book.pages[self.page_index]
                self.page_index += 1
                return page
            else:
                # Переходим к следующей книге
                self.book_index += 1
                self.page_index = 0
                return self.__next__()  # Рекурсивно вызываем, чтобы получить следующую страницу
        else:
            raise StopIteration  # Если книги закончились, останавливаем итерацию




# Пример использования
book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Используем вложенный итератор для обхода страниц в библиотеке
for page in library:
    print(page)
