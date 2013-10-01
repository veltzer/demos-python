#!/usr/bin/python

"""
This example shows that when map is given a generator it DOES NOT create a list
with all the elements that the generator provides but rather iterates the generator
added one element at a time to the resulting list.

		Mark Veltzer <mark@veltzer.net>
"""

def my_gen():
	for i in xrange(10):
		print("my_gen")
		yield i**2
def plus1(x):
	print("plus1")
	return x+1
map(plus1,my_gen())
