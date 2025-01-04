"""
Ниже в коде представлена реализация карточной колоды при помощи классов Card и Deck.

Исправьте код так, чтобы не было ошибок, и вывод программы соответствовал тестовому значению
"""


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} {self.suit}"  # Удобный формат вывода карты


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self.cards)  # Возвращаем итератор по списку карт


deck = Deck()
for card in deck:
    print(card)
