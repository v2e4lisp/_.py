import unittest
import random
import copy
import sys
from test_helper import *
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _max, _min, _shuffle, _flatten, _group_by, _count_by, _union, _dict, _sorted_index, _uniq, _intersection, _difference

class TestUnderscoreFunction(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_max(self):
        mx = _max(self.seq, lambda x,y : x-y)
        self.assertEqual(max(self.seq), mx)

    def test_min(self):
        mn = _min(self.seq, lambda x,y: x-y)
        self.assertEqual(min(self.seq), mn)

    def test_shuffle(self):
        shuffled = self.seq[:]
        _shuffle(shuffled)
        self.assertEqual(len(shuffled), len(self.seq))
        self.assertFalse(shuffled == self.seq)

    def test_flatten(self):
        t = [1,2,[3],[2,3,[4]]]
        self.assertEqual(_flatten(t), [1,2,3,2,3,[4]])
        self.assertEqual(_flatten(t, True), [1,2,3,2,3,4])

    def test_group_by(self):
        t = _group_by(self.seq, lambda x: x%2)
        self.assertEqual(t[0], list(range(0,10,2)))
        self.assertEqual(t[1], list(range(1,10,2)))

    def test_count_by(self):
        t = _count_by(self.seq, lambda x: x%2)
        self.assertEqual(t[0], len((range(0,10,2))))
        self.assertEqual(t[1], len((range(1,10,2))))

    def test_union(self):
        a = [1,2,3,3,4]
        b = [4,5,6,7,8]
        self.assertEqual(_union(a,b), list(range(1,9)))

    def test_intersection(self):
        a = [1,2,3,4]
        b = [2,3,4,5]
        c = [3,4,5,6]
        self.assertEqual(_intersection(a, b, c), [3,4])

    def test_uniq(self):
        a = [1,2,3,4,3,2,1]
        self.assertEqual(_uniq(a), [1,2,3,4])

    def test_difference(self):
        a = [1,2,3,4]
        b = [2,3,4,5,6]
        self.assertEqual(_difference(a, b), [1])

    def test_dict(self):
        keys = ["a", "b"]
        values = [1, 2]
        d = _dict(keys, values)
        self.assertEqual(d["a"], 1)
        self.assertEqual(d["b"], 2)

    def test_sorted_index(self):
        self.assertEqual(_sorted_index(self.seq, 6) , 7)


if __name__ == '__main__':
    unittest.main()
