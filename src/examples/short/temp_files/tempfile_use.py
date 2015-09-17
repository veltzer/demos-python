#!/usr/bin/python3

'''
Demo how to create a temp file in python
'''

import tempfile  # for NamedTemporaryFile

# delte=True is the default...
# t=tempfile.NamedTemporaryFile()
t = tempfile.NamedTemporaryFile(delete=False)

print('name is [{0}]'.format(t.name))
