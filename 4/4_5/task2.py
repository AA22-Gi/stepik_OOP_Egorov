"""
Рейтинг шахматистов
Для выражения относительной силы шахматистов используется система рейтингов.
Наиболее популярная система рейтингов, которая используется Международной шахматной федерацией (ФИДЕ),
большинством других шахматных федераций и игровых шахматных сайтов, – система рейтингов Эло.

В зависимости от выступлений на различных соревнованиях каждому шахматисту начисляются баллы в его рейтинг.
Давайте с вами реализуем класс ChessPlayer и научимся сравнивать рейтинги шахматистов между собой.

Итак, ваша задача — реализовать класс ChessPlayer, который состоит из:

    метода инициализации, принимающего аргументы name, surname, rating;

    магического  метода __eq__, который будет позволять сравнивать экземпляры класса ChessPlayer
    с числами и другими экземплярами этого класса. Если сравнение происходит с целым числом
    и атрибут rating с ним совпадает, то необходимо вернуть True, в противном случае - False.
    Если же сравнение идет с другим шахматистом (экземпляром класса ChessPlayer)
    и значения атрибутов rating равны, то возвращается True, в противном случае - False.
    А если же сравнивается с другим типом данных, верните «Невозможно выполнить сравнение»;

    магического  метода __gt__. Если сравнение происходит с целым числом и атрибут rating больше его,
    необходимо вернуть значение True, в противном же случае - False.
    Если сравнение происходит с другим шахматистом (экземпляром класса ChessPlayer)
    и атрибут rating у нашего экземпляра больше, то верните True, в противном случае - False.
    В случае, если сравнение идет с остальными типами данных, верните «Невозможно выполнить сравнение»;

    магического  метода __lt__. Если сравнение происходит с целым числом и атрибут rating меньше его,
    необходимо вернуть значение True, в противном же случае - False.
    Если сравнение происходит с другим шахматистом (экземпляром класса ChessPlayer)
    и атрибут rating у нашего экземпляра меньше, то верните True, в противном случае - False.
    В случае, если сравнение идет с остальными типами данных, верните «Невозможно выполнить сравнение».
"""


class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'


if __name__ == '__main__':
    magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
    assert magnus.name == 'Carlsen'
    assert magnus.surname == 'Magnus'
    assert magnus.rating == 2847
    ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
    assert not magnus == 4000
    assert ian == 2789
    assert not magnus == ian
    assert magnus > ian
    assert not magnus < ian
    assert (magnus < [1, 2]) == 'Невозможно выполнить сравнение'

    v1 = ChessPlayer('Гарри ', 'Каспаров', 10)
    v2 = ChessPlayer('Бобби', 'Фишер', 20)
    v3 = ChessPlayer('Bot', 'Bot', 20)

    assert isinstance(v1, ChessPlayer)
    assert isinstance(v2, ChessPlayer)
    assert v2.__dict__ == {'name': 'Бобби', 'surname': 'Фишер', 'rating': 20}
    assert v1.__dict__ == {'name': 'Гарри ', 'surname': 'Каспаров', 'rating': 10}
    assert v1 > 5
    assert not v1 > 10
    assert not v1 > 11
    assert not v1 < 5
    assert not v1 < 10
    assert v1 < 11
    assert not v1 == 5
    assert v1 == 10
    assert not v1 == 11
    assert not v1 > v2
    assert not v1 == v2
    assert v3 == v2
    assert not v3 != v2
    assert v1 < v2
    assert (v1 > 'fdsfd') == 'Невозможно выполнить сравнение'
    assert (v1 < 'fdsfd') == 'Невозможно выполнить сравнение'
    assert (v1 == 'fdsfd') == 'Невозможно выполнить сравнение'
    assert (v1 == [1, 2]) == 'Невозможно выполнить сравнение'
    assert (v1 < [1, 2]) == 'Невозможно выполнить сравнение'
    print('Good')
