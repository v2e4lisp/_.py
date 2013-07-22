import unittest
import random
import copy
import sys
from test_helper import *
_ = import_()

class TestUnderscoreDict(unittest.TestCase):

    def setUp(self):
        self.sample = _({"a": 1, "b": 2, "c": [3]})

    def test_value(self):
        self.assertEqual(self.sample.value(), {"a": 1, "b": 2, "c": [3]})

    def test_new(self):
        fake = copy.deepcopy(self.sample)
        self.assertEqual(fake.value(), self.sample.value())
        self.assertNotEqual(fake, self.sample)

    def test_size(self):
        self.assertEqual(self.sample.size()._, 3)

    def test_list(self):
        self.assertEqual(self.sample.list().sort()._, ['a', 'b', 'c'])

    def test_pick(self):
        self.assertEqual(self.sample.pick("b")._, {"b": 2})

    def test_omit(self):
        self.assertEqual(self.sample.omit("a", "c", "d")._, {"b": 2})

    def test_invert(self):
        t = _({"a": 1, "b": 2, "c": 3})
        self.assertEqual(t.invert().value(),
                         {1: "a", 2: "b", 3: "c"})

    def test_dict(self):
        self.assertEqual(self.sample.dict()._, {"a": 1, "b": 2, "c": [3]})

    def test_defaults(self):
        self.sample.defaults(**{"a": 1,"d": 4})
        self.assertEqual(self.sample._, {"a": 1, "b": 2, "c": [3], "d": 4})

    @python2_only
    def test_has_key (self):
        self.assertTrue(self.sample.has_key('a'))
        self.assertFalse(self.sample.has_key('fdsa'))

    def test_is_a(self):
        self.assertTrue(self.sample.is_a(dict))

    @python2_only
    def test_iteritems (self):
        self.assertEqual(type(self.sample.iteritems()._).__name__, 'dictionary-itemiterator')
        self.assertEqual(self.sample.iteritems().list().sort()._,
                         sorted([("a", 1), ("b", 2), ("c", [3])]))

    @python2_only
    def test_iterkeys (self):
        self.assertEqual(type(self.sample.iterkeys()._).__name__, 'dictionary-keyiterator')
        self.assertEqual(self.sample.iterkeys().list().sort()._,
                         sorted(["a", "b", "c"]))

    @python2_only
    def test_itervalues (self):
        self.assertEqual(type(self.sample.itervalues()._).__name__, 'dictionary-valueiterator')
        self.assertEqual(self.sample.itervalues().list().sort()._,
                         sorted([1,2,[3]]))

    def test_popitem (self):
        t = {'a': 1, 'b': 2, 'c': [3]}
        self.assertEqual(self.sample.popitem()._, t.popitem())
        self.assertEqual(self.sample._, t)

    def test_pop (self):
        self.assertEqual(self.sample.pop('a')._, 1)
        self.assertEqual(self.sample._, {'b': 2, 'c': [3]})

    def test_get (self):
        self.assertEqual(self.sample.get('a')._, 1)
        self.assertEqual(self.sample.get('x', 1)._, 1)

    def test_keys (self):
        self.assertEqual(self.sample.keys().list().sort()._, sorted(["a", "b", "c"]))

    @python2_only
    def test_values(self):
        self.assertEqual(self.sample.values().sort()._, [1,2,[3]])

    def test_values_3(self):
        self.assertEqual(_({"a": 1, "b": 2, "c": 3}).values().list().sort()._, [1,2,3])

    # def keys
    # def values
    # def items
    # def has_key
    # def iteritems
    # def iterkeys
    # def itervalues
    # def popitem
    # def get
if __name__ == '__main__':
    unittest.main()
