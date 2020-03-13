from basic_math import BasicMath
import unittest


class TestBasicMath(unittest.TestCase):

    def test_add(self):
        result = BasicMath().add(1, 2)
        self.assertEqual(result, 3)

    def test_sub(self):
        result = BasicMath().sub(3, 1)
        self.assertEqual(result, 2)
