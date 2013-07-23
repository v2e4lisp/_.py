from underscore import _Underscore, _
import helper
import random
import math
from functools import reduce

class Number_(_Underscore):
    # number object bought from ruby
    def times(self, fn):
        """
        call fn self._ times
        @param  : function()
        @return : _(number)

        e.g.
        def p(): print('s')
        _(3).times(p)
        => s
        => s
        => s
        """
        for i in range(0, self._):
            fn()
        return self

    def ceil(self):
        """
        math.ceil
        @param  : none
        @return : _(float)

        e.g.
        _(1.2).ceil()._
        => 2.0
        """
        return _(math.ceil(self._))

    def floor(self):
        """
        math.floor
        @param  : none
        @return : _(float)

        e.g.
        _(1.2).floor()._
        => 1.0
        """
        return _(math.floor(self._))

    def chr(self):
        """
        builtin chr
        @param  : none
        @return : _(str)

        e.g.
        _(65).chr()._
        'A'
        """
        return _(chr(self._))

    def even(self):
        """
        check if the number is even
        @param  : none
        @return : bool

        e.g.
        _(2).even()
        => True
        """
        return self._ % 2 == 0

    def odd(self):
        """
        check if the number is odd.
        @param  : none
        @return : bool

        e.g.
        _(2).odd()
        => False
        """
        return not self.even()

    def succ(self):
        """
        @param  : none
        @return : _(int)

        e.g.
        _(2).succ()._
        => 3
        """
        return _(self._ + 1)

    def pred(self):
        """
        @param  : none
        @return : _(int)

        e.g.
        _(2).pred()._
        => 1
        """
        return _(self._ - 1)

    def int(self):
        """
        convert to integer
        @param  : none
        @return : _(int)

        e.g.
        _(2.3).int()._
        2
        """
        return _(int(self._))

    def up_to(self, n, l):
        """
        iterate from `self._` to `n` pass the number to function `fn`.
        @param  : int
        @param  : function(int)
        @return : _(int)

        e.g.
        result = []
        _(5).down_to(1, lambda x: result.append(x))
        print result
        => [5,4,3,2]
        """
        for i in range(self._, n):
            l(i)
        return self

    def down_to(self, n, fn):
        """
        iterate from `self._` to `n` pass the number to function `fn`.
        @param  : int
        @param  : function(int)
        @return : _(int)

        e.g.
        result = []
        _(5).down_to(1, lambda x: result.append(x))
        print result
        => [5,4,3,2]
        """
        for i in range(self._, n, -1):
            fn(i)
        return self

class Iterable_(object):
    def __contains__(self, item):
        ''' in operator '''
        return item in self._

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
        return _(helper._group_by(self._, func))

    def count_by(self, func=bool):
        """
        count each element in each group. `func` default is bool
        @param  : `function(a) -> b`
        @return : `_(dict)`

        e.g.
        _([1,2,3,4,5]).count_by(lambda x: x%2)._
        => {1: 3, 0: 2}
        """
        return _(helper._count_by(self._, func))

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

class _Subscriptable(object):
    def __getitem__(self, key):
        return self._[key]

    def __setitem__(self, key, value):
        self._[key] = value
        return self

class _Indexable(object):


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
        """
        return all but first n items. n deafult is 1.
        @param  : int
        @return : _

        e.g.
        _([1,2,3,4]).rest()._
        => [2,3,4]
        """
        return _(self._[n:])

class Set_(_Underscore, Iterable_): pass

class List_(_Underscore, _Subscriptable, Iterable_, _Indexable):
    def shuffle(self):
        """
        @param  : `none`
        @return : `_`

        e.g.
        _([1,2,3]).shuffle()._
        => ...
        """
        random.shuffle(self._)
        return self

class Tuple_(_Underscore, _Subscriptable, Iterable_, _Indexable): pass


class Dict_(_Underscore, _Subscriptable, Iterable_):
    def pick(self, *keys):
        """
        get a new dict by picking from `self._ ` by `keys`
        @param  : *keys
        @return : _(dict)

        e.g.
        _({"a": 1, "b": 2}).pick("a")._
        => {"a": 1}
        """
        return _({k: self[k] for k in keys})

    def omit(self, *keys):
        """
        get a new dict by filtering out keys from self._
        @param  : *keys
        @return : _(dict)

        e.g.
        _({"a": 1, "b": 2, "c": 2}).omit("b", "c")._
        => {"a": 1}
        """
        return _({k: self[k] for k in self._ if k not in keys})

    def invert(self):
        """
        invert dict's key and value
        @param  : none
        @return : _(dict)

        e.g.
        _({"k1": "v1", "k2": "v2"}).invert()._
        {"v1": "k1", "v2": "k2"}
        """
        return _({self[k]: k for k in self._})

    def defaults(self, **kwargs):
        """
        add key and value to self._ only if key is not in self._ .
        @param  : *kwargs
        @return : _(dict)

        e.g.
        _({"a":1}).default({"a":2, "b": 3})._
        => {"a": 1, "b": 3}
        """
        for i in kwargs:
            self._.setdefault(i, kwargs[i])
        return self


class Str_(_Underscore, _Subscriptable, Iterable_, _Indexable):
    def levenshtein(self, s):
        return _(helper._levenshtein(self._, s))
        ld = levenshtein

class Nonsense_(_Underscore): pass
