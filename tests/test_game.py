from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        grid = game.grid

        # verify
        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

        # teardown


    def test_is_valid(self):
        #setup
        game = Game()
        test_grid = "KLSWTRXZO"
        test_word = "SLOW"

        #exercise
        game.grid = list(test_grid)

        #verfiy
        assert game.is_valid(test_word) is True

        #teardown
        assert game.grid == list(test_grid)


    def test_is_invalid(self):
        #setup
        game = Game()
        test_grid = "KLSWTRXZO"
        test_word = "TROTT"

        #exercise
        game.grid = list(test_grid)

        #verify
        assert game.is_valid(test_word) is False

        #teardown
        assert game.grid == list(test_grid)


    def test_empty_is_invalid(self):
        #setup
        game = Game()

        #verify
        assert game.is_valid("") is False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
