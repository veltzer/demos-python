#!/usr/bin/python

from __future__ import print_function

'''
Example for catching all exception types.
'''

try:
	raise ValueError('hello')
# this next line catches all exceptions, logs and throws them back...
except Exception,e:
	print('in except',e)
	raise e
finally:
	print('finally is here')
