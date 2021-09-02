class Card:
    """Object to represent a Card"""

    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def show(self):
        """Show the card"""
        return f"{self.name} of {self.suit}"

    def show_value(self):
        """Show the card's value"""
        return f"{self.value} of {self.suit}"
