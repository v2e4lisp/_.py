import collections
from functools import reduce

# --------------------
# - helper functions -
# --------------------

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
