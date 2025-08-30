import unittest

from core.board import Board
from core.checker import Checker

class TestBoard(unittest.TestCase):
    def test_initial_positions(self):
        
        board = Board()
        board.setup_initial_positions()

        total_white = sum(len(p) for p in board.__points__ if p and p[0].get_color() == "white")
        total_black = sum(len(p) for p in board.__points__ if p and p[0].get_color() == "black")

        self.assertEqual(total_white, 15)
        self.assertEqual(total_black, 15)

        self.assertEqual(len(board.get_point(23)), 2)
        self.assertEqual(len(board.get_point(12)), 5)
        self.assertEqual(len(board.get_point(0)), 2)
        self.assertEqual(len(board.get_point(11)), 5)

if __name__ == "__main__":
    unittest.main()   