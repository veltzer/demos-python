#!/usr/bin/python3

'''
This example shows how to convert unicode to ascii in python.

The solution here is to convert to ascii and ignore all errors.
Not the best solution but OK for some cases.

References:
- http://stackoverflow.com/questions/4299675/python-script-to-convert-from-utf-8-to-ascii
'''

s=u'\u05d4\u05d9hello'
print(type(s))
print(s)
r=s.encode("ascii", "ignore").decode("utf8")
print(type(r))
print(r)
