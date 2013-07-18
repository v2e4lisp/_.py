import unittest
import random
import copy
import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _

class TestUnderscoreNumber(unittest.TestCase):
    def test_times(self):
        a = []
        _(10).times(lambda : a.append(1))
        self.assertEqual(a, [1] * 10)


if __name__ == '__main__':
    unittest.main()
