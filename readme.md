A python collection wrapper class
=================================

- implemented half of the underscore.js funtionality (collection, array, object)
- all the built-in methods are still available on _ object.

Usage & Example
-----
** map **
```python
_([1,2,3,4]).map(lambda x: x+1)._
=> [2,3,4,5]
```

** each **
```python
def printit(it):
    print(it)
_([1,2,3]).each(printit)
=> 1
=> 2
=> 3
=> <underscore._ object at ....>
```
** reduce **
```python
_([1,2,3]).reduce(lambda t, i: t-i)._
=> -4
```
** reduce_right **
```python
_([1,2,3]).reduce_right(lambda t, i: t-i)._
=> 0
```
*to be continued*
