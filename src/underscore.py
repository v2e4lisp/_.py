import random
import helper
import copy
import math
import collections
from functools import reduce

# delegator...
class _call(object):

    '''
    proxy class recieve an function, and an _ object
    return an _ object
    '''

    def __init__(self, fn, obj):
        self.fn = fn
        self.obj = obj

    def __call__(self, *args, **kwargs):
        r = self.fn(*args, **kwargs)
        if isinstance(r, bool):
            return r
        elif r is None:
            return self.obj
        else:
            return _(r)


# underscore class
class _Underscore(object):

    '''
    a python container(and number) wrapper
    with some useful methods bought from underscore.js and ruby
    _(for).cascade._
    '''

    __delegate_methods_alias = {"index_of": "index",
                                "sort_by" : "sort"}

    def __init__(self, data):
        if not isinstance(data, _Underscore):
            self._ = data

    def __new__(cls, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], _Underscore):
            return args[0]
        return object.__new__(cls)

    def __getstate__(self):
        """
        in python3 if you inherit from object
        the __getstate__ won't work any more, which means
        you can't copy.deepcopy an instance of this class.
        This is a fix
        """
        return self._

    def __setstate__(self, state):
        self._ = state

    def __getattr__(self, name):
        ''' delegate undefined methods to self.value() '''
        name = self.__delegate_methods_alias.get(name, name)
        return _call(getattr(self._, name), self)

    def value(self):
        """
        get the value out of the _ object
        @param  : `none`
        @return : `self._`

        e.g.
        _([1,2,3]).value()
        => [1,2,3]
        # which is the same as _([1,2,3])._
        """
        return self._

#----------------------- collections -----------------------

    def copy(self, deep=False):
        """
        (deep or shallow) copy `self._`. `deep` default is `False`
        @param  : `bool`
        @return : `_`

        e.g.
        _a = _([1,2,3])
        b = _a.copy()
        b == _a._
        => True

        b.append('hello')
        b == _a._
        => False
        """
        return _(copy.deepcopy(self._) if deep else copy.copy(self._))

    def deep_copy(self):
        """
        deep copy self._
        @param  : `none`
        @return : `_`

        e.g.
        _a = _([1,2,[3]])
        b = _a.copy()
        b == _a._
        => True

        b[-1].append('4')
        print b
        => [1,2,[3,4]]
        print _a._
        => [1,2,[3]]
        """
        return self.copy(True)

    def clone(self):
        """
        shallow copy
        @param  : `none`
        @return : `_`

        e.g.
        _a = _([1,2,[3]])
        b = _a.copy()
        b == _a._
        => True
        """
        return self.copy(False)


    def compact(self):
        """
        it's equivalent to `reject(lambda x: bool(x))`
        @param  : none
        @return : _

        e.g.
        _(['', None, False, 0]).compact()._
        => []
        """
        return self.filter()

    def flatten(self, deep=False):
        """
        flatten a list, when `deep` is set to `True`,
        this will recursively flatten the whole list.
        `deep` default is `False`
        @param  : bool
        @return : _

        e.g.
        _([1,2,[3], [[4]]]).flatten()._
        => [1,2,3,[4]]

        _([1,2,[3], [[4]]]).flatten(True)._
        => [1,2,3,4]
        """
        return _(helper._flatten(self._, deep))

    def without(self, *args):
        """
        remove any item in `args` from `self._`
        @param  : *args
        @return : _

        e.g.
        _([1,2,2,3,4,1]).without(2,1)._
        => [3,4]
        """
        return self.reject(lambda x: x in args)

    def union(self, *lists):
        """
        merge `*lists` if there is any. and delete duplicated items.
        if self._ is a set, then the return _ object holds a set.
        @param  : *lists
        @return : _

        e.g.
        _([1,2,2,3]).union()._
        => [1,2,3]

        _([1,2,2,3]).union([2,3,4], [4,5])._
        => [1,5]

        # set
        _({1,2,3,4}).union([1,2,6])._
        => set([1,2,3,4,6])
        """
        if self.is_a(set):
            return _(self._.union(*lists))
        return _(helper._union(self._, *lists))

    def intersection(self, *lists):
        """
        self._ and lists intersection.
        if self._ is a set, then the return _ object holds a set.
        @param  : *lists
        @return : _

        e.g.
        _([1,2,2,3]).intersection([2,3,4], [2,5])._
        => [2]

        # set
        _({1,2,3,4}).intersection([1,2,6])._
        => set([1,2])
        """
        if self.is_a(set):
            return _(self._.intersection(*lists))
        return _(helper._intersection(self._, *lists))

    def uniq(self):
        """
        no duplicated items.
        @param  : none
        @return : _

        e.g.
        _([1,2,3,2]).uniq()._
        => [1,2,3]
        """
        return _(helper._uniq(self._))

    def difference(self, *lists):
        """
        items in self._ but not present in lists
        if self._ is a set, then the return _ object holds a set.
        `diff` is its alias.
        @param  : *lists
        @return : _

        e.g.
        _([1,2,2,3]).differece([2,3,4], [2,5])._
        => [1]

        # set
        _({1,2,3,4}).difference([1,2,6])._
        => set([3,4])
        """
        if self.is_a(set):
            return _(self._.difference(*lists))
        return _(helper._difference(self._, *lists))
    diff = difference

    def zip(self, *lists):
        """
        merge self._ and lists in a way that each time pick one item from each of the lists
        and self._ , then make a tuple out of it.
        @param  : *lists
        @return : _

        e.g.
        _([1,2,3,4]).zip([1,2,3])._
        => [(1,1), (2,2), (3,3)]
        """
        return _(zip(self._, *lists))

    def dict_values(self, values):
        """
        make a `dict` with `values` as value and `self._` as key
        @param  : a
        @return : _(dict)

        e.g.
        _(['a', 'k']).dict_values((1,2))._
        => {'a': 1, 'k': 2}
        """
        return _(helper._dict(self._, values))

    def dict_keys(self, keys):
        """
        make a `dict` with keys as key and self._ as value
        @param  : a
        @return : _(dict)

        e.g.
        _([1,2,3]).dict_keys(['a', 'b', 'c'])._
        => {'a': 1, 'b': 2, 'c': 3}
        """
        return _(helper._dict(keys, self._))

    def last_index(self, item):
        """
        return the last index of item in `self._`.
        since it use the builtin `index` method, if no such item found
        it will raise ValueError.
        `last_index_of` is its alias.

        e.g.
        _([1,3,2,3]).last_index(3)._
        => 3
        """
        return _(self.size()._ - 1 - self.reverse().index(item)._)
    last_index_of = last_index

    def sorted_index(self, item):
        """
        Uses a binary search to determine the index at which the value should be
        inserted into the list in order to maintain the list's sorted order
        the return index will be as large as possible. see the examples.
        @param  : a
        @return : _(int)

        e.g.
        _([1,2,3,4,5,6]).sorted_index(4)._
        => 4

        _([1,2,3,4,4,4,5,6]).sorted_index(4)._
        => 6
        """
        return _(helper._sorted_index(self._, item))

    def pairs(self):
        """
        list of lists containing two items.
        if self._ is dict then it will be key-value tuple.
        @param  : none
        @return : _([(a,b)])

        e.g.
        _([1,2,3,4,5]).pairs()._
        => [[1,2], [3,4], [5]]

        _({"a": 1, "b": 2}).pairs()._
        => [("a", 1), ("b", 2)]
        """
        return self.items() if self.is_a(dict) else self.chunks(2)

    def chunks(self, n):
        """
        divide the self._ into n-size list
        @param  : int
        @return : _([[a]])

        e.g.
        _([1,2,3,4]).chunks(3)._
        => [[1,2,3], [4]]
        """
        return _([self._[i:i+n] for i in range(0, self.size()._, n)])

    def is_a(self, t):
        """
        test if self._ is a `t`.
        @param  : type
        @return : bool

        e.g.
        _([1,2,3,4]).is_a(list)
        => True
        """
        return isinstance(self._, t)

    def pluck(self, key):
        """
        extracting a list of property values from self._ which is a list of dict
        @param  : a
        @return : _([])

        e.g.
        _([{"a": 1, "b": 2}, {"a": 3, "c": 4}]).pluck("a")._
        => [1,3]
        """
        return self.map(lambda x: x[key])

    def join(self, sep):
        """
        concat a list of strings by sep which is string,
        and if sep is a list of string then concat the sep by self._
        @param  : [str] || str
        @return : _(str)

        e.g.
        _(['a', 'b']).join('/')._
        => 'a/b'

        _('/').join(['a', 'b'])._
        => 'a/b'
        """
        if self.is_a(str):
            return _(self._.join(sep))
        return _(sep.join(self._))

# ------------------------------------ conversion -----------------------------
    def list(self):
        return _(list(self._))

    def dict(self):
        return _(dict(self._))

    def set(self):
        return _(set(self._))

    def str(self):
        return _(str(self._))

def _(data):
    ''' factory function. '''
    t = type(data)
    if t is set:
        return Set_(data)
    elif t is list:
        return List_(data)
    elif t is int or t is float:
        return Number_(data)
    elif t is tuple:
        return Tuple_(data)
    elif t is dict:
        return Dict_(data)
    elif t is str:
        return Str_(data)
    elif t is collections.Iterable:
        return Iterable_(data)
    else:
        return Nonsense_(data)

from datatype import *
