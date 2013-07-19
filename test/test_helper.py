# helper functions for unittest
import sys
from types import FunctionType as function

def import_():
    sys.path.append("/Users/wenjunyan/_py/src")
    sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
    from underscore import _
    return _

def python2_only(m):
    if sys.version_info.major < 3:
        return m
    else:
        return True

def python3_only(m):
    if sys.version_info.major == 3:
        return m
    else:
        return True
