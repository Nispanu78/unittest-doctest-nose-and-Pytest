import unittest

class TestClass08(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test case1()")

    def test_case02(self):
        x = 5 + 3
        z = 5 + 2
        self.assertEqual(x, z)
        print("\nIn test case 2()")

    def test_case03(self):
        self.assertTrue("python".isupper())
        print("is \nIn test case 3()")