#!/usr/bin/python3

'''
This script checks the syntax of other python scripts.
It returns a bad error code to the parent if something goes wrong.

It's basically a more sophisticated version of something like this:
	python2 -m py_compile $< || python3 -m py_compile $<
'''

import sys # for argv, exit
import subprocess # for check_call

if len(sys.argv)!=2:
	print('usage: {0} [filename]'.format(sys.argv[0]), file=sys.stderr)
	sys.exit(1)

filename=sys.argv[1]

# read the first line of the file
with open(filename, 'r') as f:
	line=f.readline().rstrip()

if line=='#!/usr/bin/python2':
	exe='python2'
elif line=='#!/usr/bin/python3':
	exe='python3'
else:
	print('{0}: found bad first line: [{1}]'.format(sys.argv[0], line), file=sys.stderr)
	sys.exit(1)

# check the syntax
subprocess.check_call([
	exe,
	'-m',
	'py_compile',
	filename,
])
