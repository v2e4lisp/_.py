import random
import collections
import copy
import math
from sys import version_info
if version_info.major > 2:
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
class _(object):

    '''
    a python container(and number) wrapper
    with some useful methods bought from underscore.js and ruby
    _(for).cascade._
    '''

    __delegate_methods_alias = {"index_of": "index",
                                "sort_by" : "sort"}

    def __init__(self, data):
        if not isinstance(data, _):
            self._ = data

    def __new__(cls, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], _):
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

    def __getitem__(self, key):
        return self._[key]

    def __setitem__(self, key, value):
        self._[key] = value
        return self

    def __getattr__(self, name):
        ''' delegate undefined methods to self.value() '''
        name = self.__delegate_methods_alias.get(name, name)
        return _call(getattr(self._, name), self)

    def __contains__(self, item):
        ''' in operator '''
        return item in self._

    def value(self):
        """
        get the value out of the _ object
        @param  : `none`
        @return : `self._`

        e.g.
        _([1,2,3]).value()
        => [1,2,3]
        which is the same as _([1,2,3])._
        """
        return self._

#----------------------- collections -----------------------

    def each(self, func):
        """
        apply the `func` to every item
        type: function -> _
        @param  : `function(a)`
        @return : `_`

        e.g.
        def printit(it): print(it)
        _([1,2,3]).each(printit)
        => 1
        => 2
        => 3
        """

        for i in self._:
            func(i)
        return self

    def map(self, func):
        """
        apply `func` to every item, and collect the result.
        @param  : `function(a) -> b`
        @return : `_`

        e.g.
        _([1,2,3]).map(lambda x: x+1)._
        => [2,3,4]
        """
        return _(map(func, self._))

    def reduce(self, func, init=None):
        """
        left-fold the self._ by `func` with initial value set to `init`
        @param  : `function(t, s) -> t`
        @param  : `init=t`
        @return : `_`

        e.g.
        _([1,2,3]).reduce(lambda t, x: t-x)._
        => -4
        """
        return _(reduce(func, self._, init) if init else reduce(func, self._))

    def reduce_right(self, func, init=None):
        """
        right-fold the self._ by `func` with initial value set to `init`
        @param  : `function(t, s)`
        @param  : `init=t`
        @return : `_`

        e.g.
        _([1,2,3]).reduce_right(lambda t, x: t-x)._
        => 0
        """
        return self.reverse().reduce(func, init)

    def filter(self, func=bool):
        """
        looks through the self._ and collect the items that passed
        `func`(return true). the default `func` is `bool`.
        @param  : `function(a) -> bool`
        @return : `_`

        e.g.
        _([1,2,3,4]).filter(lambda x: x % 2 == 0)._
        => [2,4]
        """
        return _(filter(func, self._))

    def find_item(self, func):
        """
        find the first item when `func(item)` reutrn `True`.
        it return as soon as it finds such an item.
        @param  : `function(a) -> bool`
        @return : `_(a) || None`

        e.g.
        _([1,2,2,4]).find_item(lambda x: x == 2)._
        => 2
        """
        return next((_(x) for x in self._ if func(x)), None)

    def find_where(self, cond):
        """
        find the first item whoses (key, value) pair matches `cond`
        @param  : `dict`
        @return : `_(dict) || None`

        e.g.
        _([{"a": 1, "b":2}, {"c":1, "d":2}]).find_where({"a":1})._
        => {"a": 1, "b": 2}
        """
        return self.find_item(lambda x: _(x).contains(cond))

    def where(self, cond):
        """
        find all items whose (key, value) pairs matches `cond`
        @param  : `dict`
        @return : `_([dict])`

        e.g.
        _([{"a": 1, "b":2}, {"a": 1, "b":1}, {"c":1, "d":2}]).find_where({"a":1})._
        => [{"a": 1, "b":2}, {"a": 1, "b":1}]
        """
        return self.filter(lambda x: _(x).contains(cond))

    def reject(self, func=bool):
        """
        collect items which dosen't pass the `func`(return `False`)
        `func` default is `bool`
        @param  : `function(a) -> bool`
        @return : `_`

        e.g.
        _([1,2,3,4]).reject(lambda x: x%2 == 0)._
        => [1,3]
        """
        return self.filter(lambda x: not func(x))

    def all(self, func=bool):
        """
        check if all items can pass the `func`(return `True`)
        `func` default is bool. `every` is an alias of `all`.
        @param  : `function(a) -> bool`
        @return : `bool`

        e.g.
        _([1,2,3]).all(lambda x: x>0)
        => True
        """
        return all(map(func, self._))
    every = all

    def some(self, func=bool):
        """
        check if any item in self._ can pass the `func`(return `True`)
        func default is bool. `any` is an alias of `some`
        @param  : `function(a) -> bool`
        @return : `bool`

        e.g.
        _([1,2,3]).some(lambda x: x>2)
        => True
        """
        for i in self._:
            if func(i):
                return True
    any = some

    def contains(self, item):
        """
        check if item is part of self._
        @param  : `a`
        @return : `bool`

        e.g.
        _([1,2,3]).contains(1)
        => True
        _({'a': 1,'b': 2, 'c': 3}).contains({'a':1, 'c':3})
        => True
        """
        if isinstance(item, dict):
            return _(item).all(lambda key: self._.get(key) == item[key])
        return item in self

    def invoke(self, method, *args, **kwargs):
        """
        invoke method with args on every item
        @param  : `function`
        @param  : `*args`
        @param  : `**kwargs`
        @return : `_`

        e.g.
        _([1,2,3], [3,4,5]).invoke("append", 'hello')._
        => [[1,2,3,"hello"], [1,2,3,"hello"]]
        """
        self.each(lambda x: getattr(x, method)(*args, **kwargs))
        return self

    def max(self, fn=lambda x: x):
        """
        get the max item using a key function `fn`
        `fn` default is `lambda x: x`
        @param  : `function(a) -> b`
        @return : `_(a)`

        e.g.
        _([1,2,3,4]).max(lambda x: -x)._
        => -1
        """
        return _(max(*self._, key=fn))

    def min(self, fn=lambda x: x):
        """
        get the min item using a key function `fn`
        `fn` default is `lambda x: x`
        @param  : `function(a) -> b`
        @return : `_(a)`

        e.g.
        _([1,2,3,4]).min(lambda x: -x)._
        => 4
        """
        return _(min(*self._, key=fn))

    def sorted(self, func=None):
        """
        sort the self._
        @param  : `function(a) -> k`
        @return : `_`

        e.g.
        _([3,2,1]).sorted(lambda x: x)._
        => [1,2,3]
        """
        return _(sorted(self._, key=func))

    def group_by(self, func):
        """
        group items by function, return a dict which key is generated by
        `func` and value is a list.
        @param  : `function(a) -> b`
        @return : `_(dict)`

        e.g.
        _([1,2,3,4]).group_by(lambda x: x%2)._
        => {1: [1,3], 0: [2,4]}
        """
        return _(_group_by(self._, func))

    def count_by(self, func=bool):
        """
        count each element in each group. `func` default is bool
        @param  : `function(a) -> b`
        @return : `_(dict)`

        e.g.
        _([1,2,3,4,5]).count_by(lambda x: x%2)._
        => {1: 3, 0: 2}
        """
        return _(_count_by(self._, func))

    def count(self, item):
        """
        count a certain item
        @param  : `item`
        @return : `_(int)`

        e.g.
        _([1,2,3,2,1]).count(1)._
        => 2
        """
        return _(self._.count(item))

    def shuffle(self):
        """
        @param  : `none`
        @return : `_`

        e.g.
        _([1,2,3]).shuffle()._
        => ...
        """
        _shuffle(self._)
        return self

    def size(self):
        """
        return the size of the collection
        @param  : `none`
        @return : `_(int)`

        e.g.
        _([1,2,3]).size()._
        => 3
        """
        return _(len(self._))

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

    def first(self):
        """
        get the first value . the same as self._[0]
        @param  : `none`
        @return : `_(a)`

        e.g.
        _([1,2,3]).first._
        => 1
        """
        return _(self._[0])

    def last(self):
        """
        get the last item . the same as self._[-1]
        @param  : `none`
        @return : `_(a)`

        e.g.
        _([1,2,3]).last._
        => 3
        """
        return _(self._[-1])

    def but_last(self, n=1):
        """
        return all but last n items. n default is 1.
        `take` and `initial` are its aliases.
        @param  : `int`
        @return : `_`

        e.g.
        _([1,2,3,4]).but_last()._
        => [1,2,3]
        """
        return _(self._[0:-n])
    take = initial = but_last

    def rest(self, n=1):
        return _(self._[n:])

    def compact(self):
        return self.filter()

    def flatten(self, deep=False):
        return _(_flatten(self._, deep))

    def without(self, *args):
        return self.reject(lambda x: x in args)

    def union(self, *lists):
        if self.is_a(set):
            return _(self._.union(*lists))
        return _(_union(self._, *lists))

    def intersection(self, *lists):
        if self.is_a(set):
            return _(self._.union(*lists))
        return _(_intersection(self._, *lists))

    def uniq(self):
        return _(_uniq(self._))

    def difference(self, *lists):
        if self.is_a(set):
            return _(self._.union(*lists))
        return _(_difference(self._, *lists))

    def zip(self, *lists):
        return _(zip(self._, *lists))

    def dict_values(self, values):
        return _(_dict(self._, values))

    def dict_keys(self, keys):
        return _(_dict(keys, self._))

    def last_index(self, item):
        return _(self.size()._ - 1 - self.reverse().index(item))
    last_index_of = last_index

    def sorted_index(self, item):
        return _(_sorted_index(self._, item))

    def pairs(self):
        return self.items() if self.is_a(dict) else self.chunks(2)

    def chunks(self, n):
        return _([self._[i:i+n] for i in range(0, self.size()._, n)])

    def is_a(self, t):
        return isinstance(self._, t)

    def pluck(self, key):
        return self.map(lambda x: x[key])

    def join(self, sep):
        if isinstance(self._, str):
            return _(self._.join(sep))
        return _(sep.join(self._))

#------------------------------------- dict ------------------------------

    def pick(self, *keys):
        return _({k: self[k] for k in keys})

    def omit(self, *keys):
        return _({k: self[k] for k in self._ if k not in keys})

    def invert(self):
        return _({self[k]: k for k in self._})

    def defaults(self, *args, **kwargs):
        for i in kwargs:
            self._.setdefault(i, kwargs[i])
        return self

# --------------------------------- number -------------------------------

    def times(self, l):
        for i in range(0, self._):
            l()
        return self

    def ceil(self):
        return _(math.ceil(self._))

    def floor(self):
        return _(math.floor(self._))

    def chr(self):
        return _(chr(self._))

    def down_to(self, n, l):
        for i in range(self._, n, -1):
            l(i)
        return self

    def even(self):
        return self._ % 2 == 0

    def odd(self):
        return not self.even()

    def succ(self):
        return _(self._ + 1)

    def pred(self):
        return _(self._ - 1)

    def int(self):
        return _(int(self._))

    def up_to(self, n, l):
        for i in range(self._, n):
            l(i)
        return self

# ------------------------------------ str ------------------------------------

    def levenshtein(self, s):
        return _(_levenshtein(self._, s))
    ld = levenshtein

# ------------------------------------ conversion -----------------------------
    def list(self):
        return _(list(self._))

    def dict(self):
        return _(dict(self._))

    def set(self):
        return _(set(self._))

    def str(self):
        return _(str(self._))

# --------------------
# - helper functions -
# --------------------


def _shuffle(data):
    random.shuffle(data)


def _flatten(data, deep=False):
    sub = lambda x: (isinstance(x, list) and (deep and _flatten(x, True) or x)
                     or [x])
    return reduce(lambda total, x: total + sub(x), data, [])


def _group_by(data, func):
    result = {}
    for i in data:
        key = func(i)
        if key not in result:
            result[key] = []
        result[key].append(i)
    return result


def _count_by(data, func):
    result = {}
    for i in data:
        key = func(i)
        result[key] = result[key] + 1 if key in result else 1
    return result


def _union(*lists):
    return _uniq(_flatten(lists))


def _intersection(*lists):
    return reduce(lambda r, x: [i for i in r if i in x], lists[1:], lists[0])


def _uniq(data):
    return list(collections.OrderedDict.fromkeys(data).keys())


def _difference(data, *lists):
    lists = _flatten(lists)
    return [i for i in data if i not in lists]


def _dict(keys, values):
    return dict(zip(keys, values))


def _sorted_index(data, item):
    def si(s, e):
        if s > e:
            return s
        m = int((s + e)/2)
        return si(s, m-1) if data[m] > item else si(m+1, e)
    return si(0, len(data) - 1)


def _levenshtein(s1, s2):
    l1, l2 = len(s1), len(s2)
    memo = [[None] * l2 for i in range(l1)]

    def ld(e1, e2):
        if e1 == -1:
            return e2 + 1
        if e2 == -1:
            return e1 + 1
        if memo[e1][e2] is None:
            cost = 0 if s1[e1] == s2[e2] else 1
            memo[e1][e2] = min(ld(e1-1, e2) + 1,
                               ld(e1, e2-1) + 1,
                               ld(e1-1, e2-1) + cost)
        return memo[e1][e2]

    return ld(l1-1, l2-1)
