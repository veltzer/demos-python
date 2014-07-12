#!/usr/bin/python3

'''
This is a simple example of how to use the dbm.gnu module of the
standard python library
'''

import dbm.gnu # for open

# c - open rw and create if it doesn't exist
d=dbm.gnu.open('/tmp/foo.gdbm', 'c')

d['one']='ehad'
d['two']='shtaim'

# show all key value pairs
k=d.firstkey()
while k is not None:
	print(k.decode(), d[k].decode())
	k=d.nextkey(k)

d.close()
