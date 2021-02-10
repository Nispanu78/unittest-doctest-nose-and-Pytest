from mypackage.mymathlib import *
import unittest

math_obj = 0

def setUpModule():
    """called once, before anything else in the module"""
    print("In setUpModule()...")
    global math_obj
math_obj = mymathlib()
def tearDownModule():
    """called once, after everything else in the module"""
print("In tearDownModule()...")
global math_obj
del math_obj