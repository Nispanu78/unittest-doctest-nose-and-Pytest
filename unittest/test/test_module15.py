import unittest

class Calculator():


    def add1(self, x, y):
        return x + y

    def add2(self, x, y):
        numbers = (int, float, complex)
        if isinstance(x, numbers) and isinstance (y, numbers):
            return x + y
        else:
            raise ValueError


calc = 0

class TestClass15(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global calc
        calc = Calculator()

    def setUp(self):
        print("\nIn setUp ...")

    def test_case01(self):
        self.assertEqual(calc.add1(2, 3), 5)

    def test_case02(self):
        self.assertEqual(calc.add2(3, 3), 6)

    def test_case03(self):
        self.assertRaises(ValueError, calc.add1, 2, 'two')

    def test_case04(self):
        self.assertRaises(ValueError, calc.add2, 7, 'seven')

    def tearDown(self):
        print("\nIn tear down ...")

    @classmethod
    def tearDownClass(cls):
        global calc
        del calc
