import unittest

from core.board import Board
from core.checker import Checker

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.setup_initial_positions()

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

    def test_move_checker_valid(self):
        initial_count = sum(len(p) for p in self.board.get_points())
        moved = self.board.move_checker(23, 10)  
        self.assertTrue(moved)
        final_count = sum(len(p) for p in self.get_points())
        self.assertEqual(initial_count, final_count)

    def test_move_checker_invalid(self):
        moved = self.board.move_checker(15, 5)  
        self.assertFalse(moved)

    def test_checker_changes_point(self):
        checker = self.board.get_points()[23][-1]
        self.board.move_checker(23, 10)
        self.assertIn(checker, self.board.get_points()[10])

if __name__ == "__main__":
    unittest.main()   