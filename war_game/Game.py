from Deck import Deck
from Player import Player


class Game:
    """Let's play war!"""

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = self.deck.deal([player for player in self.players])
        self.rounds = 1
    
    def game_over(self, players):
        player_status = []
        for player in players:
            if player.is_empty():
                player_status.append(True)
        
        if len(player_status) > 0:
            return True
        else:
            return False

    def play(self):
        """Let's play!"""
        while self.game_over(self.players) is False:
            for player in self.players:
                print(f"{player.name} goes first.")
                self.play_one_turn(player)
                print(f"Round {self.rounds} Complete")
                self.rounds = self.rounds + 1
        print("Game over.")
        for player in self.players:
            print(f"{player.name} won {player.rounds_won} rounds")

    def play_one_turn(self, player):
        """Play one turn for a player."""
        play_order = self.players
        if player.is_empty() is not True:
            choices = []
            for p in play_order:
                choices.append(self.play_one_turn_for(p))
            if choices[0].value >= choices[1].value:
                play_order[0].receive_cards(choices)
                p.rounds_won = p.rounds_won + 1
                print(f"{play_order[0].name} wins this round")
            else:
                play_order[1].receive_cards(choices)
                p.rounds_won = p.rounds_won + 1
                print(f"{play_order[1].name} wins this round.")


    def play_one_turn_for(self, player):
        """Play one turn for a player."""
        print(
            f"""{player.name}, has the following cards: {[card.show_value() for card in player.hand]}"""
        )
        if player.is_empty() is not True:
            choice = player.play_card()
            print(f"{player.name} chooses {choice.show()}")
            return choice
            # player.receive_cards(choice)
            # print(f"{player.name}'s hand: {[card.show() for card in player.hand]}")
        else:
            print(f"{player.name} has no cards left.")
