#!/usr/bin/python

"""
This example shows how to handle '~' in path names
"""
import os
print os.path.expanduser('~/.viminfo')
print os.path.expandvars('USER is $USER')
