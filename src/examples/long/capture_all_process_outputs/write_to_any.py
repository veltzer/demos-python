#!/usr/bin/python3

'''
This is a simple process that can log to what you want.
Examples:
[process] stdout
will log to stdout
[process] stderr
will log to stderr
[process] tty
will log to tty
and you can combine...
'''

import sys  # for stderr, argv, exit

args = sys.argv[1:]
if 'stdout' in args:
    print('this is stdout')

if 'stderr' in args:
    print('this is stderr', file=sys.stderr)

if 'tty' in args:
    f = open('/dev/tty', 'w')
    f.write('this is /dev/tty\n')
    f.close()

sys.exit(7)
