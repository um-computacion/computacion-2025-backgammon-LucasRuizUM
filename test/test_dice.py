import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        values = dice.roll()
        self.assertIsInstance(values, tuple)
        self.assertEqual(len(values), 2)

        for v in values:
            self.assertIsInstance(v, int)
            self.assertGreaterEqual(v, 1)
            self.assertLessEqual(v, 6)

    def test_multiples_rolls(self):
        dice = Dice()
        for _ in range(1000):
            values = dice.roll()
            for v in values:
                self.assertGreaterEqual(v, 1)
                self.assertLessEqual(v, 6)

if __name__ == "__main__":
    unittest.main()