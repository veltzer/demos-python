#!/usr/bin/python

'''
This example shows how to handle '~' in path names
There are two different ways: expanduser and expandvars
'''

from __future__ import print_function
import os # for expanduser, expandvars

print(os.path.expanduser('~/.viminfo'))
print(os.path.expandvars('USER is $USER'))
