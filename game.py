"This script simulates 5-card poker hands to estimate the probability of drawing a straight.
"It defines a Hand class to evaluate hand types such as flush, full house, and straight.
"Each hand is dealt from a freshly shuffled standard deck.
"The simulation continues until a straight is found or a max limit is reached.


from deck import Deck, Card
from collections import Counter


class Hand:
    def __init__(self, deck):
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        return self._cards

    @property
    def num_matches(self):
        """Count how many times each rank appears in the hand."""
        rank_counts = Counter(card.rank for card in self.cards)
        return sum(count * (count - 1) // 2 for count in rank_counts.values())

    @property
    def is_flush(self):
        """Check if all cards have the same suit."""
        return all(card.suit == self.cards[0].suit for card in self.cards)

    @property
    def is_full_house(self):
        """A full house consists of one triplet and one pair."""
        rank_counts = Counter(card.rank for card in self.cards)
        return sorted(rank_counts.values()) == [2, 3]

    @property
    def is_straight(self):
        """Check if the hand is a straight."""
        if self.num_matches != 0:
            return False
        sorted_cards = sorted(self.cards, key=lambda card: Card.RANKS.index(card.rank))
        return Card.RANKS.index(sorted_cards[-1].rank) == Card.RANKS.index(sorted_cards[0].rank) + 4

    def __str__(self):
        return str(self.cards)


# Simulating probability of a straight
matches = 0
count = 0
max_iterations = 1_000_000  # Prevent infinite loops

while matches < 10000 and count < max_iterations:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        print(hand)
        matches += 1
        break

    if count % 1000 == 0:  # Print progress every 1000 iterations
        print(f"Checked {count} hands, found {matches} straights")

if count >= max_iterations:
    print("Max iterations reached, stopping early.")

print(f"The probability of a straight is {100 * matches / count:.4f}%")

