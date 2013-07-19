import unittest
import random
import copy
import sys
from test_helper import *
_ = import_()

class TestUnderscoreNumber(unittest.TestCase):
    def test_times(self):
        a = []
        _(10).times(lambda : a.append(1))
        self.assertEqual(a, [1] * 10)

    def test_ceil (self):
        self.assertEqual(_(1.2).ceil()._, 2.0)

    def test_floor (self):
        self.assertEqual(_(1.2).floor()._, 1)

    def test_chr (self):
        self.assertEqual(_(65).chr()._, 'A')

    def test_even (self):
        self.assertIs(_(1).even(), False)
        self.assertIs(_(2).even(), True)

    def test_odd (self):
        self.assertIs(_(1).even(), False)
        self.assertIs(_(2).even(), True)

    def test_succ (self):
        self.assertEqual(_(1).succ()._, 2)

    def test_pred (self):
        self.assertEqual(_(1).pred()._, 0)

    def test_int (self):
        self.assertEqual(_(1.2).int()._, 1)

    def test_up_to (self):
        r = []
        _(5).up_to(10, lambda x: r.append(x))
        self.assertEqual(r, [5,6,7,8,9])

    def test_down_to (self):
        r = []
        _(5).down_to(0, lambda x: r.append(x))
        self.assertEqual(r, [5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()
