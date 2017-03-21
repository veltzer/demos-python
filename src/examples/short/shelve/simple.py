#!/usr/bin/python3

"""
This is a basic demo of the shelve module

Run this several times to see how it works.
"""

import shelve
import random

with shelve.open("/tmp/shelve.db") as d:
    for i in range(10):
        d[str(random.randrange(100))] = random.randrange(100)
    for k, v in d.items():
        print(k, v)
