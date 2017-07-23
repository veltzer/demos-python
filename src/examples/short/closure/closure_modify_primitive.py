#!/usr/bin/env python

"""
This is an example that shows that you cannot change primitives in closures.
"""


def make_adder():
    x = 0
    def adder():
        x += 1
        print(x)
    return adder

f = make_adder()
f()
f()
f()
