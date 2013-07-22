A python collection wrapper class
=================================

- implemented half of the underscore.js funtionality (collection, array, object)
- all the built-in methods are still available on _ object.

Usage & Example
---------------
**all**
check if all items can pass the `func`(return `True`)
func default is bool.
`every` is an alias of `all`
type: function -> boolean
_ -> boolean
```python

_([1,2,3]).all(lambda x: x>0)
=> True
```

**any**
check if any item in self._ can pass the `func`(return `True`)
func default is bool.
`any` is an alias of `some`
type: function -> boolean
_ -> boolean
```python

_([1,2,3]).some(lambda x: x>2)
=> True
```

**contains**
check if item is part of self._
type: a -> boolean
e.g
_([1,2,3]).contains(1)
=> True
_({'a': 1,'b': 2, 'c': 3}).contains({'a':1, 'c':3})
=> True
```

**each**
apply the `func` to every item
type: function -> _
```python

def printit(it): print(it)
_([1,2,3]).each(printit)
=> 1
=> 2
=> 3
```

**every**
check if all items can pass the `func`(return `True`)
func default is bool.
`every` is an alias of `all`
type: function -> boolean
_ -> boolean
```python

_([1,2,3]).all(lambda x: x>0)
=> True
```

**filter**
looks through the self._ and collect the items that passed
`func`(return true). the default `func` is `bool`.
type: -> _
function -> _
```python

_([1,2,3,4]).filter(lambda x: x % 2 == 0)._
=> [2,4]
```

**find_item**
find the first item when `func(item)` reutrn `True`.
it return as soon as it finds such an item.
type: function -> _(a)
function -> None
```python

_([1,2,2,4]).find_item(lambda x: x == 2)._
=> 2
```

**find_where**
find the first item whoses (key, value) pair matches `cond`
type: dict -> _(dict)
dict -> None
```python

_([{"a": 1, "b":2}, {"c":1, "d":2}]).find_where({"a":1})._
=> {"a": 1, "b": 2}
```

**invoke**
invoke method with args on every item
type: method * args * kwargs -> _
```python

_([1,2,3], [3,4,5]).invoke("append", 'hello')._
=> [[1,2,3,"hello"], [1,2,3,"hello"]]
```

**map**
apply `func` to every item, and collect the result.
type: function -> _
```python

_([1,2,3]).map(lambda x: x+1)._
=> [2,3,4]
```

**max**
get the max item using a key function `fn`
`fn` default is `lambda x: x`
type: function -> a
-> a
```python

_([1,2,3,4]).max(lambda x: -x)._
=> -1
```

**min**
get the min item using a key function `fn`
`fn` default is `lambda x: x`
type: function -> a
-> a
```python

_([1,2,3,4]).min(lambda x: -x)._
=> 4
```

**reduce**
left-fold the self._ by `func` with initial value set to `init`
type: function -> _
function * a -> _
```python

_([1,2,3]).reduce(lambda t, x: t-x)._
=> -4
```

**reduce_right**
right-fold the self._ by `func` with initial value set to `init`
type: function -> _(b)
function * a -> _(b)
```python

_([1,2,3]).reduce_right(lambda t, x: t-x)._
=> 0
```

**reject**
collect items which dosen't pass the `func`(return `False`)
`func` default is `bool`
type: function -> _
-> _
```python

_([1,2,3,4]).reject(lambda x: x%2 == 0)._
=> [1,3]
```

**some**
check if any item in self._ can pass the `func`(return `True`)
func default is bool.
`any` is an alias of `some`
type: function -> boolean
_ -> boolean
```python

_([1,2,3]).some(lambda x: x>2)
=> True
```

**value**
get the value out of the _ object
type: -> a
e.g
_([1,2,3]).value()
=> [1,2,3]
which is the same as _([1,2,3])._
```

**where**
find all items whose (key, value) pairs matches `cond`
type dict -> _([dict])
```python

_([{"a": 1, "b":2}, {"a": 1, "b":1}, {"c":1, "d":2}]).find_where({"a":1})._
=> [{"a": 1, "b":2}, {"a": 1, "b":1}]
```

