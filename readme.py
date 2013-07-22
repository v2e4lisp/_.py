import sys
sys.path.append("/Users/wenjunyan/_py/src")
sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
from underscore import _
import re

def p(x):
    print(x)
r = re.compile("\n\s+")
(_(dir(_))
 .filter(lambda x: getattr(_, x).__doc__ and not x.startswith('__'))
 .map(lambda x: "**"+ x + "**" + getattr(_, x).__doc__)
 .map(lambda x: r.sub("\n", x).replace("e.g.", "```python\n") + "```\n")
 .each(p))

       # .map(lambda x: x + getattr(_, x).__doc__.replace('e.g.', '```') + '```')

