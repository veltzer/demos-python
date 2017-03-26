#!/usr/bin/python3

"""
Getting the number of cores via python

Two ways to do it:
- the 'multiprocessing' module.
- the 'os' module.

NOTES:
- in python2 only 'os' module does not supply a 'cpu_count' function.
"""

import multiprocessing
import os

print(multiprocessing.cpu_count())
print(os.cpu_count())
