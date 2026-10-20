import unittest
from racunalo import sestevanje, odstevanje, mnozenje, deljenje

class TestRacunalo(unittest.TestCase):
    def test_operacije(self):
        self.assertEqual(sestevanje(5, 3), 8)
        self.assertEqual(odstevanje(5, 3), 2)
        self.assertEqual(mnozenje(5, 3), 15)
        self.assertEqual(deljenje(6, 3), 2)

if __name__ == "__main__":
    unittest.main()