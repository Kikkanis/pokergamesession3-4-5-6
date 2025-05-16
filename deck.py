#This script defines a simple playing card system with a Card and Deck class.
#It allows for creating, shuffling, and dealing cards from a standard 52-card deck.
# this was done while following in class


import random


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # Clubs = [Clubs, diamonds, hearts, spades]



    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        self._rank = rank
        self._suit = suit
    @property
    def rank(self):
       return self._rank

    @property
    def suit(self):
       return self._suit


    def __str__(self):
       return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__() # repr is the same as str
    def __eq__(selfself, other):
        return self.rank == other.rank

    def __lt__(selfself, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
       random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)






c1 = Card("A", "♣")
print(c1.suit, c1.rank)
deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print(deck.deal())
print(deck)





