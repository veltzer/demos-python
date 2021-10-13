"""
This is a demo of how to use importlib.reload to reload
modules in python.
"""

import importlib
import time
from .my_module import a


while True:
    importlib.reload(a)
    time.sleep(1)
