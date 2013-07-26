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

    __delegate_methods_alias = {"index_of": "index", "sort_by": "sort"}

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
    elif t is tuple:
        return Tuple_(data)
    elif t is dict:
        return Dict_(data)
    elif t is str:
        return Str_(data)
    elif t is int or t is float:
        return Number_(data)
    elif t is collections.Iterable:
        return Iterable_(data)
    else:
        return Nonsense_(data)

from datatype import *
