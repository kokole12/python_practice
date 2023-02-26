#!/usr/bin/python3
import unittest

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertAlmostEqual('foo'.upper(), 'FOO')
    
    def test_isUpper(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = "Hello world"
        self.assertAlmostEqual(s.split(), ["Hello", "world"])
        with self.assertRaises(TypeError):
            s.split(1)
        


if __name__ == '__main__':
    unittest.main()
