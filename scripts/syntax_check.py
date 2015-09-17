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
check_with=None
with open(filename, 'r') as f:
	for line in f:
		line=line.rstrip()
		if line=='#!/usr/bin/python2':
			check_with='python2'
			break
		elif line=='#!/usr/bin/python3':
			check_with='python3'
			break
		if line.startswith('# CHECK_WITH'):
			check_with=line.split()[2]
			break

if check_with is None:
	print('{0}: couldnt find how to check file [{1}]'.format(sys.argv[0], filename), file=sys.stderr)
	sys.exit(1)

# check the syntax
subprocess.check_call([
	check_with,
	'-m',
	'py_compile',
	filename,
])
