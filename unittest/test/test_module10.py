import unittest
from mypackage.mymathsimple import *

my_obj = 0

def setUpModule():
    print("In setUpModule()...")
    global my_obj
    my_obj = mymathsimple


def tearDownModule():
    print("In tearDownModule()...")
    global my_obj
    del my_obj

class TestClass11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass ...")

    def setUp(self):
        print("In setUp ...")

    def test_module01(self):
        self.assertEqual(mymathsimple.add(2, 3), 5)

    def test_module02(self):
        self.assertEqual(mymathsimple.mul(2,3), 7)

    def tearDown(self):
        print("In tearDown")

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass ...")
