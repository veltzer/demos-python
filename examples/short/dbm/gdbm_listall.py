#!/usr/bin/python3

'''
This is a simple example of how to use the dbm.gnu module of the
standard python library
'''

import dbm.gnu # for open

# the 'c' in the next row means open rw and create if it doesn't exist
#d=dbm.gnu.open('/home/mark/.imap_import.db', 'c')
d=dbm.gnu.open('/tmp/foo.gdbm', 'c')

# show all key value pairs
k=d.firstkey()
while k is not None:
	print(k.decode(), d[k].decode())
	k=d.nextkey(k)

d.close()
