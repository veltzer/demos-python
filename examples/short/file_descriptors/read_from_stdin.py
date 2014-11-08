#!/usr/bin/python3

'''
This is an example of how to read from a file descriptor (not a file).
'''

import os # for fdopen

for line in os.fdopen(0):
	print(line, end='')
