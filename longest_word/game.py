# pylint: disable=missing-docstring
import nltk
import string
import random

nltk.download("words")
from nltk.corpus import words

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if word == "":
            return False

        letters = self.grid.copy()

        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        return word.lower() in words.words()


if __name__ == "__main__":
    game = Game()
    game.grid = list('KWIENFUQWT')
    print(game.grid) # --> OQUWRBAZE
    my_word = "TUN"
    print(game.is_valid(my_word)) # --> True
