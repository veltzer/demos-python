#!/usr/bin/python3

'''
This example shows how to use the 'enumerate' iterator.

Notes:
- enumerate is supposed to be efficient both in python2.7
and in python3 although I haven't checked that.
'''

l=['a', 'b', 'c']
for i,c in enumerate(l):
    print(i,c)
