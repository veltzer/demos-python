#!/usr/bin/python

from __future__ import print_function

"""
Example code for raising an exception,catching it and executing finally code in python.

	Mark Veltzer <mark@veltzer.net>
"""

try:
	raise ValueError("hello")
except ValueError,e:
	print("in except",e)
finally:
	print("finally is here")
