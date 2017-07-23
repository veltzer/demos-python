#!/usr/bin/env python

"""
A basic demo of pandas
"""

from pandas import DataFrame
import numpy
import random
import string


df = DataFrame(["a", "b", "c"], index=[("0", "1"),("1","2"),("2","3")])
print(df.get_values())
try:
    print(df.ix[("0","1")])
except:
    print("yes, accessing .ix with tuple does not work")
print(df.xs(("0","1")))
