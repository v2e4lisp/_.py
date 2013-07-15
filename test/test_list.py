import unittest
import random
import copy
import sys
sys.path.append("/Users/wenjunyan/_py/src")
from underscore import _

class TestUnderscoreList(unittest.TestCase):

    def setUp(self):
        self.sample = _(range(10))
        self.sample2 = _([{"a": 1, "b": 2, "c": 3}, {"b":2, "c":3, "d":4}])

    def test_new(self):
        fake = copy.deepcopy(self.sample)
        self.assertEqual(fake.value(), self.sample.value())
        self.assertFalse(fake == self.sample)

    def test_value(self):
        self.assertEqual(self.sample.value(), range(10))

    def test_each(self):
        r = []
        func = lambda x: r.append(x)
        self.sample.each(func)
        self.assertEqual(r, self.sample.value())

    def test_map(self):
        self.assertEqual(self.sample.map(lambda x: x+1).value(),
                         list(range(1,11)))

    def test_reduce(self):
        self.assertEqual(self.sample.reduce(lambda t, x: t+x), 45)

    def test_reduce_right(self):
        self.assertEqual(self.sample.reduce_right(lambda t, x: t+x), 45)

    def test_filter(self):
        self.assertEqual(self.sample.filter(lambda x: x%2==0).value(),
                         list(range(0,10,2)))

    def test_find(self):
        self.assertEqual(self.sample.find(lambda x: x == 5), 5)
        self.assertTrue(self.sample.find(lambda x: x == 11) is None)

    def test_where(self):
        self.assertEqual(self.sample2.where({"b": 2}).value(),
                         self.sample2.value())
        self.assertEqual(self.sample2.where({"a": 1}).value(),
                         [self.sample2.value()[0]])

    def test_find_where(self):
        self.assertEqual(self.sample2.find_where({"b": 2}).value(),
                         self.sample2.value()[0])
        self.assertEqual(self.sample2.find_where({"a": 1}).value(),
                         self.sample2.value()[0])

    def test_reject(self):
        self.assertEqual(self.sample.filter(lambda x: x%2==1).value(),
                         list(range(1,10,2)))

    def test_all(self):
        self.assertTrue(self.sample.all(lambda x: x > -1))
        self.assertFalse(self.sample.all(lambda x: x > 1))

    def test_some(self):
        self.assertTrue(self.sample.some(lambda x: x > 4))
        self.assertFalse(self.sample.some(lambda x: x > 10))

    def test_contains(self):
        self.assertTrue(self.sample.contains(2))
        self.assertFalse(self.sample.contains(121))

    def test_invoke(self):
        r = []
        func = lambda x: r.append(x)
        self.assertTrue(isinstance(self.sample.invoke(func), _))
        self.assertEqual(r, list(range(0,10)))

    def test_pluck(self):
        self.assertEqual(self.sample2.pluck("b").value(), [2,2])

    def test_max(self):
        self.assertEqual(self.sample.max(), 9)
        self.assertEqual(self.sample.max(lambda x, y: y - x), 0)

    def test_min(self):
        self.assertEqual(self.sample.min(), 0)
        self.assertEqual(self.sample.max(lambda x, y: x - y), 9)

    def test_reverse(self):
        self.assertEqual(self.sample.reverse().value(), list(range(9, -1, -1)))

    def test_sort_by(self):
        self.assertEqual(self.sample.sort_by(lambda x: -x).value(),
                         self.sample.reverse().value())

    def test_group_by(self):
        t = self.sample.group_by(lambda x: x%2).value()
        self.assertEqual(t[0], list(range(0,10,2)))
        self.assertEqual(t[1], list(range(1,10,2)))

    def test_count_by(self):
        t = self.sample.count_by(lambda x: x%2).value()
        self.assertEqual(t[0], len((range(0,10,2))))
        self.assertEqual(t[1], len((range(1,10,2))))

    def test_shuffle(self):
        shuffled = copy.deepcopy(self.sample)
        self.sample.shuffle()
        self.assertEqual(len(shuffled.value()), len(self.sample.value()))
        self.assertFalse(shuffled.value() == self.sample.value())

    def test_size(self):
        self.assertEqual(self.sample.size(), 10)

    def to_list(self):
        self.assertEqual(self.sample.to_list().value(), list(range(0,10)))

    def list(self):
        self.assertEqual(self.sample.to_list().value(), list(range(0,10)))

    # def test_flatten(self):
    #     t = [1,2,[3],[2,3,[4]]]
    #     self.assertEqual(_flatten(t), [1,2,3,2,3,[4]])
    #     self.assertEqual(_flatten(t, True), [1,2,3,2,3,4])

    # def test_union(self):
    #     a = [1,2,3,3,4]
    #     b = [4,5,6,7,8]
    #     self.assertEqual(_union(a,b), list(range(1,9)))

    # def test_intersection(self):
    #     a = [1,2,3,4]
    #     b = [2,3,4,5]
    #     c = [3,4,5,6]
    #     self.assertEqual(_intersection(a, b, c), [3,4])

    # def test_uniq(self):
    #     a = [1,2,3,4,3,2,1]
    #     self.assertEqual(_uniq(a), [1,2,3,4])

    # def test_difference(self):
    #     a = [1,2,3,4]
    #     b = [2,3,4,5,6]
    #     self.assertEqual(_difference(a, b), [1])

    # def test_dict(self):
    #     keys = ["a", "b"]
    #     values = [1, 2]
    #     d = _dict(keys, values)
    #     self.assertEqual(d["a"], 1)
    #     self.assertEqual(d["b"], 2)

    # def test_sorted_index(self):
    #     self.assertEqual(_sorted_index(self.seq, 6) , 7)

if __name__ == '__main__':
    unittest.main()
