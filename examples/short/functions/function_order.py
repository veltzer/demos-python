#!/usr/bin/python

"""
This example explores function ordering

	Mark Veltzer <mark@veltzer.net>
"""
# this is wrong
#foo()

def foo():
	print("this is foo")
	bar()

# this is wrong...
#foo()

def bar():
	print("this is bar")

foo()
del bar
foo()
