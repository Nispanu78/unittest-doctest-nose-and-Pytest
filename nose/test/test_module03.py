from mypackage.mymathlib import *
import unittest

calc = 0

def setUpModule():
    print("\nIn setUpModule() ...")
    global calc
    calc = mymathlib()

def tearDownModule():
    print("\nIn tearDownModule() ...")
    global calc
    del calc


class TestClass11():
    @classmethod
    def setUpClass(cls):
        print("\nIn setUpClass() ...")

    def setUp(self):
        print("\nIn setUp ...")

    def test_method01(self):
        print("\n In test_case01")
        assert calc.add(2, 3) == 5

    def test_method02(self):
        print("in test_case02")

    def tearDown(self):
        print("\nIn tearDown ...")

    @classmethod
    def tearDownClass(cls):
        print("\nIn tear down ...")
