from main import parabola
import unittest

class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(parabola(5), 25)

    def test_second(self):
        self.assertEqual(parabola(-5), 25)

    def test_third(self):
        self.assertEqual(parabola(0), 0)

if __name__ == '__main__':
    unittest.main()