#!/usr/bin/python

"""
This is an example of doing our own xrange

	Mark Veltzer <mark@veltzer.net>
"""

def my_xrange(fr,to,jump):
	while fr<to:
		yield fr
		fr+=jump

for i in my_xrange(1,13,3):
	print i
