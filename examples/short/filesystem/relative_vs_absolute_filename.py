#!/usr/bin/python3

'''
This example shows how to know, in python, whether the file name
that you get is realtive or absolute
'''

import os.path # for isabs
import sys # for stdin

for line in sys.stdin:
	# remove white space
	line=line.strip()
	if os.path.isabs(line):
		print('absolute')
	else:
		print('relative')
