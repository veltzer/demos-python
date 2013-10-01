#!/usr/bin/python

"""
This example shows how to use the os chdir command.
Note that an exception is thrown if a directory name which cannot be
changed to is supplied (bad name, access problem and more).

	Mark Veltzer <mark@veltzer.net>
"""
import os

# a wrong directory on purpose...
try:
	os.chdir('/tmpi')
except:
	print('yes, got an exception for a bad directory')
os.chdir('/tmp')
os.system('ls')
