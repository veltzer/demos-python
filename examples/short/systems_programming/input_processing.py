#!/usr/bin/python

'''
This example is similar to while(<>) in perl which processes input
both from standard input and from command line arguments.
'''

from __future__ import print_function
import fileinput

for line in fileinput.input():
	line=line.rstrip()
	print(line)
