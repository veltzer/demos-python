#!/usr/bin/python3

"""
A basic demo of the lmdb module

By default the files that will be created in the folder you specify
are 'data.mdb' and 'lock.mdb'.
"""

import lmdb

env=lmdb.open('/tmp', map_size=1000000000000)
with env.begin(write=True) as txn:
    k=bytes('hello','utf8')  # Data on disk is a byte array...
    v=bytes('world','utf8')  # ...so explicitly state the encoding!

    txn.put(k,v)                   # read
    v=txn.get(k,default='what??')  # write

    v=str(v,'utf8')          # again: Explicitly state the encoding!
    print(v)
