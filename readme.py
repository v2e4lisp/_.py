import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _
import re

def p(x): print(x)
(_(dir(_))
 .filter(lambda x: getattr(_, x).__doc__ and not x.startswith('__'))
 .map(lambda x: "### "+ x + getattr(_, x).__doc__)
 .map(lambda x: x.replace("        ", "").replace("e.g.", "```python\n").replace("type", "\n**type**") + "```\n")
 .map(lambda x: x.replace("@param", "\n**@param**"))
 .map(lambda x: x.replace("@return", "\n**@return**"))
 .each(p))

