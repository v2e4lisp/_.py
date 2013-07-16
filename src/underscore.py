# underscore module
import random
import collections as CL
import operator as OP
import copy as CP

def _max(data, func=None):
    if func:
        return reduce(lambda r, x : (func(r, x) < 0) and x or r, data[1:], data[0])
    else:
        return max(data)

def _min(data, func=None):
    if func:
        return reduce(lambda r, x : (func(r, x) > 0) and x or r, data[1:], data[0])
    else:
        return max(data)

def _shuffle(data): random.shuffle(data)

def _flatten (data, deep=False):
    return reduce(lambda total, x: total + (isinstance(x, list)
                                            and (deep and _flatten(x, True) or x)
                                            or [x]),
                  data, [])

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

# underscore class

class _(object):
    def __init__(self, data):
        if not isinstance(data, _):
            self._ = data

    def __new__(cls, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], _):
            return data
        return object.__new__(cls)

    def value(self): return self._

#----------------------- underscore.js collections -----------------------

    def each (self, func):
        for i in self._: func(i)
        return self

    def map (self, func): return _(map(func, self._))

    def reduce (self, func, init = None):
        return reduce(func, self._, init) if init else reduce(func, self._)

    def reduce_right (self, func, init = None):
        return self.reverse().reduce(func, init)

    def filter (self, func=bool): return _(filter(func, self._))

    def find (self, func):
        for i in self._:
            if func(i): return i

    def where (self, cond):
        return self.filter(lambda x: all(map(lambda key: x.has_key(key) and x[key] == cond[key], cond)))

    def find_where (self, cond):
        return _(self.find(lambda x: all(map(lambda key: x.has_key(key) and x[key] == cond[key], cond))))

    def reject (self, func=bool): return self.filter (lambda x: not func(x))

    def all (self, func=bool): return all(map(func, self._))
    every = all

    def some (self, func=bool):
        for i in self._:
            if func(i): return True

    def contains (self, item): return item in self._

    def invoke (self, method, *args, **kwargs):
        self.each(lambda x: getattr(x, method)(*args, **kwargs))
        return self

    def max (self, func=None): return _max(self._, func) if func else max(self._)

    def min (self, func=None): return _min(self._, func) if func else min(self._)

    def sort_by (self, func): return _(sorted (self._, key=func))

    def group_by (self, func): return _(_group_by(self._, func))

    def count_by (self, func=bool): return _(_count_by(self._, func))

    def shuffle (self): return _shuffle(self._) or self


    def size (self): return len(self._)

    def to_list (self):
        if isinstance(self._, dict) : return self._.items()
        return list(self._)

    def list(self): return _(self.to_list())

    def copy (self, deep=False): return _(CP.deepcopy(self._) if deep else CP.copy(self._))

    def deep_copy (self): return self.copy(True)

    def clone (self): return self.copy(False)

# -------------------------- underscore.js array --------------------------

    def first (self): return self._[0]

    def last (self): return self._[-1]

    def but_last (self, n=1): return _(self._[0:-n])
    initial = but_last

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

    def index (self, item): return self._.index(item)
    index_of = index

    def last_index (self, item): return self.size() - 1 - self.reverse().index(item)
    last_index_of = last_index

    def sorted_index (self, item): return _sorted_index(self._, item)

# -------------------------- python list method --------------------------

    def append (self, item):
        self._.append(item)
        return self

    def extend (self, new_list):
        self._.extend(new_list)
        return self

    def insert (self, i, item):
        self._.insert (i, item)
        return self

    # shared with dict
    def pop (self, i=None): return self._.pop(i) if i else self._.pop()

    def count (self,item): return self._.count(item)

    def sort (self):
        self._.sort()
        return self

    def reverse (self):
        self._.reverse()
        return self

# -------------------------------------- dict --------------------------------------

    def keys (self): return _(self._.keys())

    def values (self): return _(self._.values())

    def items (self): return _(self._.items())

    def has_key (self, key): return self._.has_key(key)
    has = has_key

    def pick (self, *keys):
        result = {}
        that = self.deep_copy()
        for k in keys:
            result[k] = that._[k]
        return _(result)

    def omit (self, *keys):
        that = self.deep_copy()
        for k in keys:
            if k in that._: that.pop(k)
        return that

    def invert (self):
        return self.items().map(lambda t: (t[1], t[0])).dict()

    def pluck (self, key): return self.map(lambda x: x[key])

    def form_keys (self, value=None): return _(fomrkeys(self._, value))
    
    def get (self, key, default=None): return self._.get(key)

    def iter_items (self): return self._.iteritems()

    def iter_keys (self): return self._.iterkeys()

    def iter_values (self): return self._.itervalues()

    def pop_item (self): return self._.popitem()

# ------------------------------------ end of dict ------------------------------------
