from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "suit"])


class Deck:
    rank = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.rank
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = Deck()
print(deck[1:10])
