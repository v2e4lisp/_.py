import unittest
import random
import copy
import sys
from test_helper import *
_ = import_()

class TestUnderscoreList(unittest.TestCase):

    def setUp(self):
        self.sample = _(list(range(10)))
        self.sample2 = _([{"a": 1, "b": 2, "c": 3}, {"b":2, "c":3, "d":4}])

    def test_getitem(self):
        self.assertEqual(self.sample[0], 0)

    def test_setitem(self):
        s = self.sample.list()
        self.assertEqual(s[0], 0)
        s[0] = 1
        self.assertEqual(s[0], 1)

    def test_new(self):
        fake = copy.deepcopy(self.sample)
        self.assertEqual(fake.value(), self.sample.value())
        self.assertNotEqual(fake, self.sample)

    def test_value(self):
        self.assertEqual(self.sample.value(), list(range(10)))

    def test_each(self):
        r = []
        func = lambda x: r.append(x)
        self.sample.each(func)
        self.assertEqual(r, self.sample.value())

    def test_map(self):
        self.assertEqual(self.sample.map(lambda x: x+1).list().value(),
                         list(range(1,11)))

    def test_reduce(self):
        self.assertEqual(self.sample.reduce(lambda t, x: t+x)._, 45)

    def test_reduce_right(self):
        self.assertEqual(self.sample.reduce_right(lambda t, x: t+x)._, 45)

    def test_filter(self):
        self.assertEqual(self.sample.filter(lambda x: x%2==0).list().value(),
                         list(range(0,10,2)))

    def test_find_item(self):
        self.assertEqual(self.sample.find_item(lambda x: x == 5)._, 5)
        self.assertTrue(self.sample.find_item(lambda x: x == 11) is None)

    def test_where(self):
        self.assertEqual(self.sample2.where({"b": 2}).list().value(),
                         self.sample2.value())
        self.assertEqual(self.sample2.where({"a": 1}).list().value(),
                         [self.sample2.value()[0]])

    def test_find_where(self):
        self.assertEqual(self.sample2.find_where({"b": 2}).value(),
                         self.sample2.value()[0])
        self.assertEqual(self.sample2.find_where({"a": 1}).value(),
                         self.sample2.value()[0])

    def test_reject(self):
        self.assertEqual(self.sample.filter(lambda x: x%2==1).list().value(),
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
        r = _(["s", "b", "c"])
        self.assertTrue(_(r).invoke("upper")._, ["S", "B", "C"])

    def test_pluck(self):
        self.assertEqual(self.sample2.pluck("b").list().value(), [2,2])

    def test_max(self):
        self.assertEqual(self.sample.max()._, 9)
        self.assertEqual(self.sample.max(lambda x: -x)._, 0)

    def test_min(self):
        self.assertEqual(self.sample.min()._, 0)
        self.assertEqual(self.sample.min(lambda x: -x)._, 9)

    def test_reverse(self):
        self.assertEqual(self.sample.reverse().value(), list(range(9, -1, -1)))

    def test_sort_by(self):
        t = self.sample.deep_copy()
        self.assertEqual(self.sample.sort_by(key=lambda x: -x).value(),
                         t.reverse().value())

    def test_group_by(self):
        t = self.sample.group_by(lambda x: x%2).value()
        self.assertEqual(t[0], list(range(0,10,2)))
        self.assertEqual(t[1], list(range(1,10,2)))

    def test_count_by(self):
        t = _(set(range(10))).count_by(lambda x: x%2).value()
        self.assertEqual(t[0], 5)
        self.assertEqual(t[1], 5)

    def test_shuffle(self):
        shuffled = copy.deepcopy(self.sample)
        self.sample.shuffle()
        self.assertEqual(len(shuffled.value()), len(self.sample.value()))
        self.assertNotEqual(shuffled.value(), self.sample.value())

    def test_size(self):
        self.assertEqual(self.sample.size()._, 10)

    def test_list(self):
        self.assertEqual(self.sample.list()._, list(range(0,10)))

    def test_copy(self):
        t = _({"a": 1, "b": 2, "c": [1]})
        shallow = t.copy()
        deep = t.copy(True)
        self.assertEqual(t.value(), shallow.value())
        self.assertEqual(t.value(), deep.value())
        self.assertIsNot(t.value(), shallow.value())
        self.assertIsNot(t.value(), deep.value())
        self.assertIs(t.value()["c"], shallow.value()["c"])
        self.assertIsNot(t.value()["c"], deep.value()["c"])

    def test_deep_copy(self):
        t = _({"a": 1, "b": 2, "c": [1]})
        deep = t.deep_copy()
        self.assertEqual(t.value(), deep.value())
        self.assertIsNot(t.value(), deep.value())
        self.assertIsNot(t.value()["c"], deep.value()["c"])

    def test_clone(self):
        t = _({"a": 1, "b": 2, "c": [1]})
        shallow = t.copy()
        self.assertEqual(t.value(), shallow.value())
        self.assertIsNot(t.value(), shallow.value())
        self.assertIs(t.value()["c"], shallow.value()["c"])

    def test_first(self):
        self.assertEqual(self.sample.first()._, self.sample[0])

    def test_last(self):
        self.assertEqual(self.sample.last()._, self.sample[-1])

    def test_but_last(self):
        self.assertEqual(self.sample.but_last().value(),
                         self.sample.value()[:-1])
        self.assertEqual(self.sample.but_last(2).value(),
                         self.sample.value()[:-2])

    def test_rest(self):
        self.assertEqual(self.sample.rest().value(), self.sample.value()[1:])
        self.assertEqual(self.sample.rest(2).value(), self.sample.value()[2:])

    def test_compact(self):
        t = _([1, "", 2, False, None])
        self.assertEqual(t.compact().list().value(), [1,2])

    def test_flatten(self):
        t = _([1,[2],[[3]],4])
        self.assertEqual(t.flatten().value(), [1,2,[3],4])
        self.assertEqual(t.flatten(True).value(), [1,2,3,4])

    def test_without(self):
        self.assertEqual(self.sample.without(1,2,3,4,5).list().value(), [0,6,7,8,9])

    def test_union(self):
        a = [1,2,3,3,4]
        b = [4,5,6,7,8]
        self.assertEqual(_(a).union(b)._, list(range(1,9)))

    def test_intersection(self):
        a = [1,2,3,4]
        b = [2,3,4,5]
        c = [3,4,5,6]
        self.assertEqual(_(a).intersection(b, c)._, [3,4])

    def test_uniq(self):
        a = [1,2,3,4,3,2,1]
        self.assertEqual(_(a).uniq()._, [1,2,3,4])

    def test_difference(self):
        a = [1,2,3,4]
        b = [2,3,4,5,6]
        self.assertEqual(_(a).difference(b)._, [1])

    def test_zip(self):
        self.assertEqual(self.sample.zip(range(10, 20)).list().value(),
                         self.sample.map(lambda x: (x, x+10)).list().value())

    def test_dict(self):
        t = [("a", 1), ("b", 2)]
        self.assertEqual(_(t).dict()._, {"a": 1, "b": 2})

    def test_dict_values(self):
        keys = ["a", "b"]
        values = [1, 2]
        self.assertEqual(_(keys).dict_values(values)._, {"a": 1, "b": 2})

    def test_dict_values(self):
        keys = ["a", "b"]
        values = [1, 2]
        self.assertEqual(_(values).dict_keys(keys)._, {"a": 1, "b": 2})

    def index(self):
        self.assertEqual(self.sample.index(5), 5)

    def last_index(self):
        t = list(range(10) + range(5,15))
        self.assertEqual(_(t).last_index(9), 23)

    def test_sorted_index(self):
        self.assertEqual(self.sample.sorted_index(6)._ , 7)

    def test_append(self):
        t = list(range(10))
        t.append(11)
        self.assertEqual(self.sample.list().append(11).value(), t)

    def test_extend(self):
        t = list(range(10, 20))
        t1 = list(range(10))
        t1.extend(t)
        self.assertEqual(self.sample.extend(t).value(), t1)

    def test_insert(self):
        t = list(range(10))
        t.insert(10, 10)
        self.assertEqual(self.sample.insert(10,10).value(), t)

    def test_pop(self):
        t = list(range(10))
        self.sample.pop()
        t.pop()
        self.assertEqual(self.sample.value(), t)

    def test_count(self):
        t = list(range(10)) + list(range(20))
        self.assertEqual(_(t).count(8)._, t.count(8))

    def test_sort(self):
        t1 = [2,3,51,5,6,2,3,1,6,7]
        t2 = t1[:]
        t1.sort()
        self.assertEqual(_(t2).sort()._, t1)

    def test_reverse(self):
        t1 = [2,3,51,5,6,2,3,1,6,7]
        t2 = t1[:]
        t1.reverse()
        self.assertEqual(_(t2).reverse()._, t1)

    def test_chunks(self):
        self.assertEqual(self.sample.chunks(3)._,
                         [[0,1,2],[3,4,5],[6,7,8],[9]])

    def test_pairs(self):
        self.assertEqual(self.sample.pairs()._,
                         [[0,1],[2,3],[4,5],[6,7],[8,9]])

    def test_is_a(self):
        self.assertTrue(self.sample.is_a(list))

    def test_times(self):
        a = []
        _(10).times(lambda : a.append(1))
        self.assertEqual(a, [1] * 10)


if __name__ == '__main__':
    unittest.main()
