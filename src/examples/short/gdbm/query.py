#!/usr/bin/python3

"""
This is an example of how to query the values in a gdbm file.
"""

import dbm.gnu

filename = "/tmp/test.gdbm"
# the 'r' in the next line means open for read only
d = dbm.gnu.open(filename, 'r')

print('ehad in db', 'ehad' in d)
print('one in db', 'one' in d)
print(d["one"])

d.close()
