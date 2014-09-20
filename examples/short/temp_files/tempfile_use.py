#!/usr/bin/python

'''
Demo how to create a temp file in python

	Mark Veltzer <mark@veltzer.net>
'''

import tempfile # for NamedTemporaryFile

# delte=True is the default...
#t=tempfile.NamedTemporaryFile()
t=tempfile.NamedTemporaryFile(delete=False)

print('name is [{0}]'.format(t.name))
