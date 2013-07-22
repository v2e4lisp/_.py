import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _
import re

def p(x):
    print(x)
r = re.compile("        ")
(_(dir(_))
 .filter(lambda x: getattr(_, x).__doc__ and not x.startswith('__'))
 .map(lambda x: "**"+ x + "**\n" + getattr(_, x).__doc__)
 .map(lambda x: r.sub("", x).replace("e.g.", "```python\n").replace("type", "\n/type/") + "```\n")
 .each(p))

