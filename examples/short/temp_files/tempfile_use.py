#!/usr/bin/python

'''
Demo how to create a temp file in python

	Mark Veltzer <mark@veltzer.net>
'''

import tempfile # for NamedTemporaryFile

#t=tempfile.NamedTemporaryFile(delete=True)
t=tempfile.NamedTemporaryFile()

print('name is [{0}]'.format(t.name))
