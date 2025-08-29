import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        p = Player("Lucas")

        s = str(p)
        self.assertIn("Lucas", s)
        self. assertIn("15", s)


if __name__ == "__main__":
    unittest.main()