#!/usr/bin/python2

'''
Example code for raising an exception,catching it and executing finally code in python.
'''

from __future__ import print_function

try:
	raise ValueError('hello')
except ValueError,e:
	print('in except',e)
finally:
	print('finally is here')
