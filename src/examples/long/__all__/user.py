#!/usr/bin/env python

from module import *

a()
try:
    b()
except NameError as _:
    print("yes got exception")
