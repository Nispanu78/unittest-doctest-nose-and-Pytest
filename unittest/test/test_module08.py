import unittest
import MyTest

class TestModule09(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(MyTest.add(3, 3), 5)
        print("\nIn test_case01")

    def test_case02(self):
        self.assertEqual(MyTest.mul(5, 5), 25)
        print("\nIn test_case02")
