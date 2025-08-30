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

    def test_set_color(self):
        c = Checker("white")
        c.set_color("black")
        self.assertEqual(c.get_color(), "black")

   

if __name__ == "__main__":
    unittest.main()
