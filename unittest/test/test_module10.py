import unittest
from mypackage.mymathsimple import *

simple_math = 0

def setUpModule():
    global simple_math
    simple_math = mymathsimple()

def tearDownModule():
    global simple_math
    simple_math = mymathsimple()

class TestClass11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUp class ...")

    def setUp(self):
        print("In setUp ...")

    def test_case01(self):
        self.assertEqual(mymathsimple.add(5, 4), 10)

    def tearDown(self):
        print("In tearDown")

    @classmethod
    def tearDownClass(cls):
        print("In setUp class ...")
