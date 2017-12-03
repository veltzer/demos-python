#!/usr/bin/env python

"""
This example shows how to use itertools.islice to cut down on the number
of iteration that a loop does...

It also shows how to write your own islice implementation....
"""

from itertools import islice

# This is the most basic example: getting only the first n elements
# from an interable. When islice gets one argument it's meaning is 'stop'.
for i in islice(range(10), 5):
    print(i)
# start and stop
for i in islice(range(10), 2, 7):
    print(i)
# start, stop and step
for i in islice(range(10), 4, 14, 2):
    print(i)


def simple_islice(iterable, size:int):
    for i, x in enumerate(iterable):
        if i == size:
            break
        yield x

for i in simple_islice(range(10), 5):
    print(i)
for i in simple_islice(range(10), 10):
    print(i)
for i in simple_islice(range(10), 11):
    print(i)
