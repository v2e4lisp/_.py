import unittest
import random
import copy
import sys
from test_helper import *
_ = import_()

class TestUnderscoreSet(unittest.TestCase):
    def setUp(self):
        # cool syntax!
        self.s = _({1,2,3,4,5})
        self.raw = {1,2,3,4,5}

    def test_value (self):
        self.assertEqual(self.s.value(), self.raw)

    def test_new (self):
        fake = copy.deepcopy(self.s)
        self.assertEqual(fake.value(), self.s.value())
        self.assertNotEqual(fake, self.s)

    def test_size (self):
        self.assertEqual(self.s.size()._, 5)

    def test_list (self):
        self.assertEqual(self.s.list().sort()._, [1,2,3,4,5])

    def test_contains (self):
        self.assertTrue(self.s.contains(1))
        self.assertFalse(self.s.contains(10))

    def test_each(self):
        r = []
        func = lambda x: r.append(x)
        self.s.each(func)
        self.assertEqual(r, self.s.list().sort()._)

    def test_map(self):
        self.assertEqual(self.s.map(lambda x: x+1).list().sort()._, [2,3,4,5,6])

    def test_reduce(self):
        self.assertEqual(self.s.reduce(lambda t, x: t+x)._, 15)

    def test_filter(self):
        self.assertEqual(self.s.filter(lambda x: x%2==0).list().value(), [2, 4])

    def test_find_item(self):
        self.assertEqual(self.s.find_item(lambda x: x == 5)._, 5)
        self.assertTrue(self.s.find_item(lambda x: x == 11) is False)

    def test_reject(self):
        self.assertEqual(self.s.reject(lambda x: x%2==1).list().sort()._, [2, 4])

    def test_all(self):
        self.assertTrue(self.s.all(lambda x: x > -1))
        self.assertFalse(self.s.all(lambda x: x > 1))

    def test_some(self):
        self.assertTrue(self.s.some(lambda x: x > 4))
        self.assertFalse(self.s.some(lambda x: x > 10))

    def test_invoke(self):
        r = _({"s", "b", "c"})
        self.assertTrue(_(r).invoke("upper")._, {"S", "B", "C"})

    def test_max(self):
        self.assertEqual(self.s.max()._, 5)
        self.assertEqual(self.s.max(lambda x:  -x)._, 1)

    def test_min(self):
        self.assertEqual(self.s.min()._, 1)
        self.assertEqual(self.s.min(lambda x: -x)._, 5)

    def test_group_by(self):
        t = self.s.group_by(lambda x: x%2).value()
        self.assertEqual(t[0], [2,4])
        self.assertEqual(t[1], [1,3,5])

    def test_count_by(self):
        t = self.s.count_by(lambda x: x%2).value()
        self.assertEqual(t[0], 2)
        self.assertEqual(t[1], 3)

    #-------------------------builtin----------------------------


if __name__ == '__main__':
    unittest.main()
