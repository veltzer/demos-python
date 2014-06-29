#!/usr/bin/python3

'''
example of how to work with standard input in python.
This program copies data from standard input into standard
output line by line.
'''

import sys # for stdin

for x in sys.stdin:
	print(x,end='')
