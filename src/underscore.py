import random
import collections as CL
import operator as OP
import copy as CP
import math

# underscore class


class _call(object):

    ''' proxy class recieve an function, and an _ object
    return an _ object
    '''

    def __init__(self, fn, obj):
        self.fn = fn
        self.obj = obj

    def __call__(self, *args, **kwargs):
        r = self.fn(*args, **kwargs)
        return _(r) if r else self.obj

class _(object):

    def __init__(self, data):
        if not isinstance(data, _):
            self._ = data

    def __new__(cls, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], _):
            return data
        return object.__new__(cls)

    def __getitem__ (self, key): return self._[key]

    def __setitem__ (self, key, value):
        self._[key] = value
        return self

    def __getattr__(self, name):
        return _call(getattr(self._, name), self)

    def value(self): return self._

#----------------------- collections -----------------------

    def each (self, func):
        for i in self._: func(i)
        return self

    def map (self, func): return _(map(func, self._))

    def reduce (self, func, init = None):
        return _(reduce(func, self._, init) if init else reduce(func, self._))

    def reduce_right (self, func, init = None):
        return self.reverse().reduce(func, init)

    def filter (self, func=bool): return _(filter(func, self._))

    def find (self, func):
        for i in self._:
            if func(i): return _(i)

    def where (self, cond):
        return self.filter(lambda x: all(map(lambda key: x.has_key(key) and x[key] == cond[key], cond)))

    def find_where (self, cond):
        return self.find(lambda x: all(map(lambda key: x.has_key(key) and x[key] == cond[key], cond)))

    def reject (self, func=bool): return self.filter(lambda x: not func(x))

    def all (self, func=bool): return all(map(func, self._)) and self
    every = all

    def some (self, func=bool):
        for i in self._:
            if func(i): return self
    any = some

    def contains (self, item): return (item in self._) and self

    def invoke (self, method, *args, **kwargs):
        self.each(lambda x: getattr(x, method)(*args, **kwargs))
        return self

    def max (self, func=None): return _(_max(self._, func) if func else max(self._))

    def min (self, func=None): return _(_min(self._, func) if func else min(self._))

    def sort_by (self, func): return _(sorted (self._, key=func))

    def group_by (self, func): return _(_group_by(self._, func))

    def count_by (self, func=bool): return _(_count_by(self._, func))

    def shuffle (self):
        _shuffle(self._)
        return self

    def size (self): return _(len(self._))

    def list (self):
        return _(self._.items()) if self.is_a(dict) else _(list(self._))

    def copy (self, deep=False):
        return _(CP.deepcopy(self._) if deep else CP.copy(self._))

    def deep_copy (self): return self.copy(True)

    def clone (self): return self.copy(False)

    def first (self): return _(self._[0])

    def last (self): return _(self._[-1])

    def but_last (self, n=1): return _(self._[0:-n])
    take = initial = but_last

    def rest (self, n=1): return _(self._[n:])

    def compact (self): return self.filter()

    def flatten (self, deep=False): return _(_flatten(self._, deep))

    def without (self, *args): return self.reject(lambda x: x in args)

    def union (self, *lists): return _(_union(self._, *lists))

    def intersection (self, *lists): return _(_intersection(self._, *lists))

    def uniq (self): return _(_uniq(self._))

    def difference (self, *lists): return _(_difference(self._, *lists))

    def zip (self, *lists): return _(zip(self._, *lists))

    def dict (self): return _(dict(self._))

    def dict_values (self, values): return _(_dict(self._, values))

    def dict_keys (self, keys): return _(_dict(keys, self._))

    def index (self, item): return _(self._.index(item))
    index_of = index

    def last_index (self, item):
        return _(self.size()._ - 1 - self.reverse().index(item))
    last_index_of = last_index

    def sorted_index (self, item): return _(_sorted_index(self._, item))

    def pairs (self):
        return self.items() if self.is_a(dict) else self.chunks(2)

    def chunks (self, n):
        return _([self._[i:i+n] for i in range(0, self.size()._, n)])

    def is_a (self, t): return isinstance(self._, t) and self

# -------------------------- python list method --------------------------
# following method are send it to the actual list
    # append
    # extend
    # insert
    # pop
    # sort
    # reverse


# -------------------------------------- dict --------------------------------------

    # def keys (self): return _(self._.keys())

    # def values (self): return _(self._.values())

    # def items (self): return _(self._.items())

    def has_key (self, key): return self._.has_key(key) and self
    has = has_key

    def pick (self, *keys):
        return _({k: self[k] for k in keys})

    def omit (self, *keys):
        return _({k: self[k] for k in self._ if k not in keys})

    def invert (self):
        return _({self[k]: k for k in self._})

    def defaults (self, d, **kwargs):
        for x in (d, kwargs):
            for i in x:
                self._.setdefault(i, x[i])
        return self

    def pluck (self, key): return self.map(lambda x: x[key])

    def form_keys (self, value=None): return _(fomrkeys(self._, value))

    # def iter_items (self): return _(self._.iteritems())

    # def iter_keys (self): return _(self._.iterkeys())

    # def iter_values (self): return _(self._.itervalues())

    # def pop_item (self): return _(self._.popitem())

    # def get (self, key): return _(self[key])

# ------------------------------------ number ------------------------------------

    def times (self, l):
        for i in range(0, self._): l()
        return self

    def ceil (self): return _(math.ceil(self._))

    def floor (self): return _(math.floor(self._))

    def chr (self): return _(chr(self._))

    def down_to (self, n, l):
        for i in range(self._, n, -1): l(i)
        return self

    def even (self): return self._%2 == 0 and self

    def odd (self): return not self.even() and self

    def succ (self): return _(self._ + 1)

    def pred (self): return _(self._ - 1)

    def int (self): return _(int(self._))

    def up_to (self, n, l):
        for i in range(self._, n): l(i)
        return self

# ------------------------------------ str ------------------------------------
# TODO

# helper functions

def _max(data, func):
    return reduce(lambda r, x : (func(r, x) < 0) and x or r, data[1:], data[0])

def _min(data, func):
    return reduce(lambda r, x : (func(r, x) > 0) and x or r, data[1:], data[0])

def _shuffle(data): random.shuffle(data)

def _flatten (data, deep=False):
    sub = lambda x:  (isinstance(x, list) and (deep and _flatten(x, True) or x) or [x])
    return reduce(lambda total, x: total + sub(x), data, [])

def _group_by (data, func):
    result = {}
    for i in data:
        key = func(i)
        if not result.has_key(key): result[key] = []
        result[key].append(i)
    return result

def _count_by (data, func):
    result = {}
    for i in data:
        key = func(i)
        result[key] = result[key] + 1 if result.has_key(key) else 1
    return result

def _union (*lists): return _uniq(_flatten(lists))

def _intersection (*lists):
    return reduce(lambda r, x: [i for i in r if i in x], lists[1:], lists[0])

def _uniq (data): return CL.OrderedDict.fromkeys(data).keys()

def _difference (data, *lists):
    lists = _flatten(lists)
    return [i for i in data if i not in lists]

def _dict (keys, values): return dict(zip(keys, values))

def _sorted_index (data, item):
    def si (s, e):
        if s > e: return s
        m = (s + e)/2
        return si(s, m-1) if data[m] > item else si(m+1, e)
    return si(0, len(data) - 1)
