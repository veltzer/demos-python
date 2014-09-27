#!/usr/bin/python3

import sys
import itertools

def indentation(line):
	return len(line)-len(line.lstrip())

for (indent, paragraph) in itertools.groupby(sys.stdin, key=indentation):
	print('%d-spaced paragraph'%indent)
	for line in paragraph:
		print(line.strip())
