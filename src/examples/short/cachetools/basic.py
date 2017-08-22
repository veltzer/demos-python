#!/usr/bin/env python

"""
A basic example for using the 'cachetools' module
"""

from functools import lru_cache
import time

@lru_cache(maxsize=1000)
def function(a, b):
    time.sleep(2)
    return a+b

print(function(2,3))
print(function(2,3))
