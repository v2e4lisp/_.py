# helper functions for unittest
import sys
import os
from types import FunctionType as function

def import_():
    # sys.path.append("/Users/wenjunyan/_.py/src")
    # sys.path.append("/Users/wenjun.yan/tmp/_.py/src")
    sys.path.append("/".join(os.path.abspath(__file__).split("/")[0:-2])
                    + "/src")
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
