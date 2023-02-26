from operators import add, sub
import unittest

class test_operators(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
    
    def test_div(self):
        self.assertRaises(ZeroDivisionError)


if __name__ == "__main__":
    unittest.main()