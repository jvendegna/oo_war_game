import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.rounds_won = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def play_card(self):
        return self.hand.pop(random.randint(0, len(self.hand) - 1))

    def receive_cards(self, cards):
        for card in cards:
            self.hand.append(card)

    def is_empty(self):
        if len(self.hand) == 0:
            return True
        else:
            return False
