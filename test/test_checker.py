import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def test_init_color(self):
        white_checker = Checker("white")
        self.assertEqual(white_checker.__color__, "white")
        self.assertIsInstance(white_checker.__color__, str)

        black_checker = Checker("black")
        self.assertEqual(black_checker.__color__, "black")
        self.assertIsInstance(black_checker.__color__, str)

if __name__ == "__main__":
    unittest.main()
