import unittest
import main
class TestFormuleFeatures(unittest.TestCase):
    def test_formule(self):
        self.assertEqual("(a + b)^1 = a + b", main.get_formule(1))
        self.assertEqual("(a + b)^2 = a^2 + 2ab + b^2", main.get_formule(2))

if __name__ == "__main__":
    unittest.main()