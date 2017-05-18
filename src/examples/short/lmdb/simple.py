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

    txn.put(k,v)                   # write
    v=txn.get(k,default='what??')  # read

    v=str(v,'utf8')          # again: Explicitly state the encoding!
    assert v == "world"

env=lmdb.open('/tmp/file.mdb', subdir=False, max_dbs=2)
with env.begin(write=True, db="a") as txn:
    k=bytes('a_key','utf8')  # Data on disk is a byte array...
    v=bytes('a_val','utf8')  # ...so explicitly state the encoding!
    txn.put(k,v)                   # write
print(env)

with env.begin(write=False, db="a") as txn:
    v=txn.get("a_key")  # read
    v=str(v,'utf8')          # again: Explicitly state the encoding!
    print(v)
