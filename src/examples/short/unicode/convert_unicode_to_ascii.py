#!/usr/bin/python3

"""
This example shows how to convert unicode to ascii in python.

The solution here is based on the 'unidecode' module.

References:
- https://pypi.python.org/pypi/Unidecode
"""

import unidecode

s = u'ko\u017eu\u0161\u010dek'
print(type(s))
print(s)
r = s.encode("ascii", "ignore").decode("utf8")
print(type(r))
print(r)
t = unidecode.unidecode(s)
print(type(t))
print(t)
