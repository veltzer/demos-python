#!/usr/bin/python3

"""
This is a simple example of how to use the dbm.gnu module of the
standard python library

NOTES:
- the attempt to insert None as value throws an exception.
    so only strings and bytes are allowed.
"""

import dbm.gnu
import os.path

# the 'c' in the next row means open rw and create if it doesn't exist
filename = "/tmp/test.gdbm"

if os.path.isfile(filename):
    os.unlink(filename)

# n means create a new database and open for reading and writing
d = dbm.gnu.open(filename, 'n')
d['one'] = 'ehad'
d['two'] = 'shtaim'
try:
    d['three'] = None
except TypeError as e:
    print("yes, got exception when trying to put None as value")
try:
    d[None] = 'four'
except TypeError as e:
    print("yes, got exception when trying to put None as key")
d['five'] = 'five'.encode()
d.close()
