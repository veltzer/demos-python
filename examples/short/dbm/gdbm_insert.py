#!/usr/bin/python3

'''
This is a simple example of how to use the dbm.gnu module of the
standard python library

NOTES:
- the attempt to insert None as value throws an exception.
	so only strings and bytes are allowed.
'''

import dbm.gnu  # for open

# the 'c' in the next row means open rw and create if it doesn't exist
d = dbm.gnu.open('/tmp/foo.gdbm', 'c')

d['one'] = 'ehad'
d['two'] = 'shtaim'
d['three'] = None

d.close()
