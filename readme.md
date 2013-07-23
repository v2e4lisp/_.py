A python collection wrapper class
=================================

- implemented half of the underscore.js funtionality (collection, array, object)
- all the built-in methods are still available on _ object.

Usage & Example
---------------
### all(func)
check if all items can pass the `func`(return `True`)
`func` default is bool. `every` is an alias of `all`.

**@param**  : `function(a) -> bool`

**@return** : `bool`

```python

_([1,2,3]).all(lambda x: x>0)
=> True
```

### any(func)
check if any item in self._ can pass the `func`(return `True`)
func default is bool. `any` is an alias of `some`

**@param**  : `function(a) -> bool`

**@return** : `bool`

```python

_([1,2,3]).some(lambda x: x>2)
=> True
```

### but_last(n)
return all but last n items. n default is 1.
`take` and `initial` are its aliases.

**@param**  : `int`

**@return** : `_`

```python

_([1,2,3,4]).but_last()._
=> [1,2,3]
```

### ceil()
math.ceil

**@param**  : none

**@return** : _(float)

```python

_(1.2).ceil()._
=> 2.0
```

### chr()
builtin chr

**@param**  : none

**@return** : _(str)

```python

_(65).chr()._
'A'
```

### chunks(n)
divide the self._ into n-size list

**@param**  : int

**@return** : _([[a]])

```python

_([1,2,3,4]).chunks(3)._
=> [[1,2,3], [4]]
```

### clone()
shallow copy

**@param**  : `none`

**@return** : `_`

```python

_a = _([1,2,[3]])
b = _a.copy()
b == _a._
=> True
```

### compact()
it's equivalent to `reject(lambda x: bool(x))`

**@param**  : none

**@return** : _

```python

_(['', None, False, 0]).compact()._
=> []
```

### contains(item)
check if item is part of self._

**@param**  : `a`

**@return** : `bool`

```python

_([1,2,3]).contains(1)
=> True
_({'a': 1,'b': 2, 'c': 3}).contains({'a':1, 'c':3})
=> True
```

### copy(deep)
(deep or shallow) copy `self._`. `deep` default is `False`

**@param**  : `bool`

**@return** : `_`

```python

_a = _([1,2,3])
b = _a.copy()
b == _a._
=> True

b.append('hello')
b == _a._
=> False
```

### count(item)
count a certain item

**@param**  : `item`

**@return** : `_(int)`

```python

_([1,2,3,2,1]).count(1)._
=> 2
```

### count_by(func)
count each element in each group. `func` default is bool

**@param**  : `function(a) -> b`

**@return** : `_(dict)`

```python

_([1,2,3,4,5]).count_by(lambda x: x%2)._
=> {1: 3, 0: 2}
```

### deep_copy()
deep copy self._

**@param**  : `none`

**@return** : `_`

```python

_a = _([1,2,[3]])
b = _a.copy()
b == _a._
=> True

b[-1].append('4')
print b
=> [1,2,[3,4]]
print _a._
=> [1,2,[3]]
```

### defaults(**kwargs)
add key and value to self._ only if key is not in self._ .

**@param**  : *kwargs

**@return** : _(dict)

```python

_({"a":1}).default({"a":2, "b": 3})._
=> {"a": 1, "b": 3}
```

### dict_keys(keys)
make a `dict` with keys as key and self._ as value

**@param**  : a

**@return** : _(dict)

```python

_([1,2,3]).dict_keys(['a', 'b', 'c'])._
=> {'a': 1, 'b': 2, 'c': 3}
```

### dict_values(values)
make a `dict` with `values` as value and `self._` as key

**@param**  : a

**@return** : _(dict)

```python

_(['a', 'k']).dict_values((1,2))._
=> {'a': 1, 'k': 2}
```

### diff(*lists)
items in self._ but not present in lists
if self._ is a set, then the return _ object holds a set.
`diff` is its alias.

**@param**  : *lists

**@return** : _

```python

_([1,2,2,3]).differece([2,3,4], [2,5])._
=> [1]

# set
_({1,2,3,4}).difference([1,2,6])._
=> set([3,4])
```

### difference(*lists)
items in self._ but not present in lists
if self._ is a set, then the return _ object holds a set.
`diff` is its alias.

**@param**  : *lists

**@return** : _

```python

_([1,2,2,3]).differece([2,3,4], [2,5])._
=> [1]

# set
_({1,2,3,4}).difference([1,2,6])._
=> set([3,4])
```

### down_to(n, fn)
iterate from `self._` to `n` pass the number to function `fn`.

**@param**  : int

**@param**  : function(int)

**@return** : _(int)

```python

result = []
_(5).down_to(1, lambda x: result.append(x))
print result
=> [5,4,3,2]
```

### each(func)
apply the `func` to every item

**type**: function -> _

**@param**  : `function(a)`

**@return** : `_`

```python

def printit(it): print(it)
_([1,2,3]).each(printit)
=> 1
=> 2
=> 3
```

### even()
check if the number is even

**@param**  : none

**@return** : bool

```python

_(2).even()
=> True
```

### every(func)
check if all items can pass the `func`(return `True`)
`func` default is bool. `every` is an alias of `all`.

**@param**  : `function(a) -> bool`

**@return** : `bool`

```python

_([1,2,3]).all(lambda x: x>0)
=> True
```

### filter(func)
looks through the self._ and collect the items that passed
`func`(return true). the default `func` is `bool`.

**@param**  : `function(a) -> bool`

**@return** : `_`

```python

_([1,2,3,4]).filter(lambda x: x % 2 == 0)._
=> [2,4]
```

### find_item(func)
find the first item when `func(item)` reutrn `True`.
it return as soon as it finds such an item.

**@param**  : `function(a) -> bool`

**@return** : `_(a) || None`

```python

_([1,2,2,4]).find_item(lambda x: x == 2)._
=> 2
```

### find_where(cond)
find the first item whoses (key, value) pair matches `cond`

**@param**  : `dict`

**@return** : `_(dict) || None`

```python

_([{"a": 1, "b":2}, {"c":1, "d":2}]).find_where({"a":1})._
=> {"a": 1, "b": 2}
```

### first()
get the first value . the same as self._[0]

**@param**  : `none`

**@return** : `_(a)`

```python

_([1,2,3]).first._
=> 1
```

### flatten(deep)
flatten a list, when `deep` is set to `True`,
this will recursively flatten the whole list.
`deep` default is `False`

**@param**  : bool

**@return** : _

```python

_([1,2,[3], [[4]]]).flatten()._
=> [1,2,3,[4]]

_([1,2,[3], [[4]]]).flatten(True)._
=> [1,2,3,4]
```

### floor()
math.floor

**@param**  : none

**@return** : _(float)

```python

_(1.2).floor()._
=> 1.0
```

### group_by(func)
group items by function, return a dict which key is generated by
`func` and value is a list.

**@param**  : `function(a) -> b`

**@return** : `_(dict)`

```python

_([1,2,3,4]).group_by(lambda x: x%2)._
=> {1: [1,3], 0: [2,4]}
```

### initial(n)
return all but last n items. n default is 1.
`take` and `initial` are its aliases.

**@param**  : `int`

**@return** : `_`

```python

_([1,2,3,4]).but_last()._
=> [1,2,3]
```

### int()
convert to integer

**@param**  : none

**@return** : _(int)

```python

_(2.3).int()._
2
```

### intersection(*lists)
self._ and lists intersection.
if self._ is a set, then the return _ object holds a set.

**@param**  : *lists

**@return** : _

```python

_([1,2,2,3]).intersection([2,3,4], [2,5])._
=> [2]

# set
_({1,2,3,4}).intersection([1,2,6])._
=> set([1,2])
```

### invert()
invert dict's key and value

**@param**  : none

**@return** : _(dict)

```python

_({"k1": "v1", "k2": "v2"}).invert()._
{"v1": "k1", "v2": "k2"}
```

### invoke(method, *args, **kwargs)
invoke method with args on every item

**@param**  : `function`

**@param**  : `*args`

**@param**  : `**kwargs`

**@return** : `_`

```python

_([1,2,3], [3,4,5]).invoke("append", 'hello')._
=> [[1,2,3,"hello"], [1,2,3,"hello"]]
```

### is_a(t)
test if self._ is a `t`.

**@param**  :
**type**

**@return** : bool

```python

_([1,2,3,4]).is_a(list)
=> True
```

### join(sep)
concat a list of strings by sep which is string,
and if sep is a list of string then concat the sep by self._

**@param**  : [str] || str

**@return** : _(str)

```python

_(['a', 'b']).join('/')._
=> 'a/b'

_('/').join(['a', 'b'])._
=> 'a/b'
```

### last()
get the last item . the same as self._[-1]

**@param**  : `none`

**@return** : `_(a)`

```python

_([1,2,3]).last._
=> 3
```

### last_index(item)
return the last index of item in `self._`.
since it use the builtin `index` method, if no such item found
it will raise ValueError.
`last_index_of` is its alias.

```python

_([1,3,2,3]).last_index(3)._
=> 3
```

### last_index_of(item)
return the last index of item in `self._`.
since it use the builtin `index` method, if no such item found
it will raise ValueError.
`last_index_of` is its alias.

```python

_([1,3,2,3]).last_index(3)._
=> 3
```

### map(func)
apply `func` to every item, and collect the result.

**@param**  : `function(a) -> b`

**@return** : `_`

```python

_([1,2,3]).map(lambda x: x+1)._
=> [2,3,4]
```

### max(fn)
get the max item using a key function `fn`
`fn` default is `lambda x: x`

**@param**  : `function(a) -> b`

**@return** : `_(a)`

```python

_([1,2,3,4]).max(lambda x: -x)._
=> -1
```

### min(fn)
get the min item using a key function `fn`
`fn` default is `lambda x: x`

**@param**  : `function(a) -> b`

**@return** : `_(a)`

```python

_([1,2,3,4]).min(lambda x: -x)._
=> 4
```

### odd()
check if the number is odd.

**@param**  : none

**@return** : bool

```python

_(2).odd()
=> False
```

### omit(*keys)
get a new dict by filtering out keys from self._

**@param**  : *keys

**@return** : _(dict)

```python

_({"a": 1, "b": 2, "c": 2}).omit("b", "c")._
=> {"a": 1}
```

### pairs()
list of lists containing two items.
if self._ is dict then it will be key-value tuple.

**@param**  : none

**@return** : _([(a,b)])

```python

_([1,2,3,4,5]).pairs()._
=> [[1,2], [3,4], [5]]

_({"a": 1, "b": 2}).pairs()._
=> [("a", 1), ("b", 2)]
```

### pick(*keys)
get a new dict by picking from `self._ ` by `keys`

**@param**  : *keys

**@return** : _(dict)

```python

_({"a": 1, "b": 2}).pick("a")._
=> {"a": 1}
```

### pluck(key)
extracting a list of property values from self._ which is a list of dict

**@param**  : a

**@return** : _([])

```python

_([{"a": 1, "b": 2}, {"a": 3, "c": 4}]).pluck("a")._
=> [1,3]
```

### pred()

**@param**  : none

**@return** : _(int)

```python

_(2).pred()._
=> 1
```

### reduce(func, init)
left-fold the self._ by `func` with initial value set to `init`

**@param**  : `function(t, s) -> t`

**@param**  : `init=t`

**@return** : `_`

```python

_([1,2,3]).reduce(lambda t, x: t-x)._
=> -4
```

### reduce_right(func, init)
right-fold the self._ by `func` with initial value set to `init`

**@param**  : `function(t, s)`

**@param**  : `init=t`

**@return** : `_`

```python

_([1,2,3]).reduce_right(lambda t, x: t-x)._
=> 0
```

### reject(func)
collect items which dosen't pass the `func`(return `False`)
`func` default is `bool`

**@param**  : `function(a) -> bool`

**@return** : `_`

```python

_([1,2,3,4]).reject(lambda x: x%2 == 0)._
=> [1,3]
```

### rest(n)
return all but first n items. n deafult is 1.

**@param**  : int

**@return** : _

```python

_([1,2,3,4]).rest()._
=> [2,3,4]
```

### shuffle()

**@param**  : `none`

**@return** : `_`

```python

_([1,2,3]).shuffle()._
=> ...
```

### size()
return the size of the collection

**@param**  : `none`

**@return** : `_(int)`

```python

_([1,2,3]).size()._
=> 3
```

### some(func)
check if any item in self._ can pass the `func`(return `True`)
func default is bool. `any` is an alias of `some`

**@param**  : `function(a) -> bool`

**@return** : `bool`

```python

_([1,2,3]).some(lambda x: x>2)
=> True
```

### sorted(func)
sort the self._

**@param**  : `function(a) -> k`

**@return** : `_`

```python

_([3,2,1]).sorted(lambda x: x)._
=> [1,2,3]
```

### sorted_index(item)
Uses a binary search to determine the index at which the value should be
inserted into the list in order to maintain the list's sorted order
the return index will be as large as possible. see the examples.

**@param**  : a

**@return** : _(int)

```python

_([1,2,3,4,5,6]).sorted_index(4)._
=> 4

_([1,2,3,4,4,4,5,6]).sorted_index(4)._
=> 6
```

### succ()

**@param**  : none

**@return** : _(int)

```python

_(2).succ()._
=> 3
```

### take(n)
return all but last n items. n default is 1.
`take` and `initial` are its aliases.

**@param**  : `int`

**@return** : `_`

```python

_([1,2,3,4]).but_last()._
=> [1,2,3]
```

### times(fn)
call fn self._ times

**@param**  : function()

**@return** : _(number)

```python

def p(): print('s')
_(3).times(p)
=> s
=> s
=> s
```

### union(*lists)
merge `*lists` if there is any. and delete duplicated items.
if self._ is a set, then the return _ object holds a set.

**@param**  : *lists

**@return** : _

```python

_([1,2,2,3]).union()._
=> [1,2,3]

_([1,2,2,3]).union([2,3,4], [4,5])._
=> [1,5]

# set
_({1,2,3,4}).union([1,2,6])._
=> set([1,2,3,4,6])
```

### uniq()
no duplicated items.

**@param**  : none

**@return** : _

```python

_([1,2,3,2]).uniq()._
=> [1,2,3]
```

### up_to(n, l)
iterate from `self._` to `n` pass the number to function `fn`.

**@param**  : int

**@param**  : function(int)

**@return** : _(int)

```python

result = []
_(5).down_to(1, lambda x: result.append(x))
print result
=> [5,4,3,2]
```

### value()
get the value out of the _ object

**@param**  : `none`

**@return** : `self._`

```python

_([1,2,3]).value()
=> [1,2,3]
# which is the same as _([1,2,3])._
```

### where(cond)
find all items whose (key, value) pairs matches `cond`

**@param**  : `dict`

**@return** : `_([dict])`

```python

_([{"a": 1, "b":2}, {"a": 1, "b":1}, {"c":1, "d":2}]).find_where({"a":1})._
=> [{"a": 1, "b":2}, {"a": 1, "b":1}]
```

### without(*args)
remove any item in `args` from `self._`

**@param**  : *args

**@return** : _

```python

_([1,2,2,3,4,1]).without(2,1)._
=> [3,4]
```

### zip(*lists)
merge self._ and lists in a way that each time pick one item from each of the lists
and self._ , then make a tuple out of it.

**@param**  : *lists

**@return** : _

```python

_([1,2,3,4]).zip([1,2,3])._
=> [(1,1), (2,2), (3,3)]
```
