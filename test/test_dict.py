import unittest
import random
import copy
import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _

class TestUnderscoreDict(unittest.TestCase):

    def setUp(self):
        self.sample = _({"a": 1, "b": 2, "c": [3]})

    def test_value(self):
        self.assertEqual(self.sample.value(), {"a": 1, "b": 2, "c": [3]})

    def test_new(self):
        fake = copy.deepcopy(self.sample)
        self.assertEqual(fake.value(), self.sample.value())
        self.assertNotEqual(fake, self.sample)
        
    def test_get(self):
        self.assertEqual(self.sample.get('a').value(), 1)

    def test_values(self):
        self.assertEqual(self.sample.values().sort()._, [1,2,[3]])

    def test_size(self):
        self.assertEqual(self.sample.size()._, 3)

    def test_list(self):
        self.assertEqual(self.sample.list().sort()._, [('a', 1), ('b', 2), ('c', [3])])

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

    def test_is_a(self):
        self.assertTrue(self.sample.is_a(dict))

if __name__ == '__main__':
    unittest.main()

