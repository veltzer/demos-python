#!/usr/bin/python2

'''
This is an example of doing our own xrange
'''

from __future__ import print_function


def my_xrange(fr, to, jump):
    while fr < to:
        yield fr
        fr += jump

for i in my_xrange(1, 13, 3):
    print(i)
