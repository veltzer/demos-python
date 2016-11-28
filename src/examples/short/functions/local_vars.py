#!/usr/bin/python3

"""
This example shows that scope of variables in a python function
is really local
"""


def myfunc():
    x = 5
    print(x)

x = 7
myfunc()
print(x)
