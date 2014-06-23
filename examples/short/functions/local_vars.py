#!/usr/bin/python

from __future__ import print_function

def myfunc(y):
	print(locals())
	print(x)
	x=5
	print(x)
	print(locals())

x=7
myfunc(9)
print(x)
