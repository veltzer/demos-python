#!/usr/bin/python

"""
	this example shows that you can pass any generator/sequence to a function
	that only uses the generator/sequence API and get the right results.
	What can't you do? Use slices for example...

	Mark Veltzer
"""

def myfunc(s):
	for i in s:
		print i,
	print

myfunc(xrange(10))
myfunc(range(10))
myfunc((1,2,3))
myfunc([1,2,3])
myfunc("hello")
