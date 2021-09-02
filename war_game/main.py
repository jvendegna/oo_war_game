import Deck
import Player

from Game import Game


player = Player.Player("Player")
cpu = Player.Player("CPU")

game = Game([player, cpu])

game.play()
