#!/usr/bin/python3

'''
This is an example of a process which logs both to stdout and stderr
'''

import sys # for stderr

print('this is stdout')
print('this is stderr', file=sys.stderr)
