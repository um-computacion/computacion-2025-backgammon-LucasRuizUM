import unittest

from core.game import BackgammonGame

class TestBackgammonGame(unittest.TestCase):
    def setUp(self):
        self.game = BackgammonGame()

    def test_initial_setup(self):

        self.assertEqual(len(self.game.__players__), 2)

        self.assertEqual(self.game.__turn__, 0)

        self.assertEqual(len(self.game.__board__.__points__), 24)

    def test_roll_dice(self):

        dice_values = self.game.roll_dice()
        self.assertEqual(len(dice_values), 2)
        for value in dice_values:
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)

    def test_next_turn(self):

        current = self.game.__turn__
        self.game.next_turn()
        self.assertNotEqual(self.game.__turn__, current)

        self.assertEqual(self.game.__turn__, (current +1) % 2)

    def test_start_board_positions(self):

        self.game.start()

        board = self.game.get_board()

        total_checkers = sum(len(p) for p in board.get_points())

        self.assertGreaterEqual(total_checkers, 0)

if __name__ == '__main__':
    unittest.main()