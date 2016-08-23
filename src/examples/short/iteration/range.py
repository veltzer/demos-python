#!/usr/bin/python3

'''
This example shows how to use the 'range' iterator.

Notes:
- in python2.7 there was a great different in the performance
of 'range' vs. 'xrange'. 'range' built the entire list in advance
while 'xrange' only iterated the given list.
- in python3 'xrange' is gone. 'range' has the efficiency of python2.7's
'xrange' and so you don't have to worry about any of these.
'''

for i in range(10):
    print(i)
