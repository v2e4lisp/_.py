import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _
import inspect

def p(x): print(x)

def args(x):
    s = inspect.getargspec(getattr(_, x))
    r = ", ".join(s.args[1:])
    if s.varargs:
        r = r + ", *" + s.varargs
    if s.keywords:
        r = r + ", **" + s.keywords
    return r

def dl(x):
    return x + "("+ args(x) + ")"

(_(dir(_))
 .filter(lambda x: getattr(_, x).__doc__ and not x.startswith('__'))
 .map(lambda x: "### "+ dl(x) + getattr(_, x).__doc__)
 .map(lambda x: inspect.cleandoc(x).replace("e.g.", "```python\n").replace("type", "\n**type**") + "\n```\n")
 .map(lambda x: x.replace("@param", "\n**@param**"))
 .map(lambda x: x.replace("@return", "\n**@return**"))
 .each(p))


