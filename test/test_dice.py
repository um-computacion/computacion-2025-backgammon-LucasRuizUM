import unittest
from computacion_2025_backgammon_LucasRuizUM.core.dice import Dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        values = dice.roll()
        self.assertEqual(len(values), 2)
        self.assertTrue(1 <= values [0] <= 6)
        self.assertTrue(1 <= values[1] <= 6)

if __name__ == "__main__":
    unittest.main()