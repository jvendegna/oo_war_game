import random
from Card import Card


class Deck:
    """A standard deck of cards."""

    def __init__(self):
        self.cards = []
        self.build()
        for i in range(random.randint(1, 10)):
            self.shuffle()

    def __str__(self):
        """Return a string representing the deck."""
        return str(self.cards)

    def build(self):
        """Build the deck."""
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for rank in [
                ("Ace", 14),
                ("2", 2),
                ("3", 3),
                ("4", 4),
                ("5", 5),
                ("6", 6),
                ("7", 7),
                ("8", 8),
                ("9", 9),
                ("10", 10),
                ("Jack", 11),
                ("Queen", 12),
                ("King", 13),
            ]:
                self.cards.append(Card(rank[0], rank[1], suit))

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Remove a card from the deck."""
        return self.cards.pop()

    def deal(self, players):
        while len(self.cards) > 0:
            for player in players:
                player.receive_cards([self.draw_card()])
