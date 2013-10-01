#!/usr/bin/python

"""
Question: what does this function output ?

Answer: exception.

	Mark Veltzer <mark@veltzer.net>
"""
def my_mistery_function():
	#global g
	print(g)
	if False:
		g+=17
	print(g)

g=4
my_mistery_function()
print(g)
