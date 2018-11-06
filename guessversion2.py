"""
File: guessversion2.py
Lays out the user interface for a GUI-based
guessing game.
"""
import random
from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window,widgets, and data."""
        EasyFrame.__init__(self, title="Guessing Game")
        self.myNumber = random.randint(1, 100)
        self.count = 0
        self.addLabel(text="Guess a number between 1 and 100.", row=1, column=0, sticky="NSEW")
        self.hintLabel = self.addLabel(text='greetings!',
                                       row=0, column=0,
                                       sticky="NSEW",
                                       columnspan=2)
        self.addLabel(text="Your guess", row=2, column=0)
        self.guessField = self.addIntegerField(0, row=2, column=1)
        self.nextButton = self.addButton(text="Next", row=3, column=0, command=self.game)
        self.newButton = self.addButton(text="New game", row=3, column=1)

    def game(self):
        number = self.guessField.getNumber()
        actual = self.myNumber
        if number == actual:
            self.messageBox(title="Correct!", message="you guessed correctly!!")
        if number != actual:
            self.messageBox(title="guess Again!", message="you guessed Incorrectly, guess again!")


def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
