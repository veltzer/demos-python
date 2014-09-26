#!/usr/bin/python

'''
Demo to show the usage of the global function 'reload'
'''

from __future__ import print_function
import imp

import using_reload_one
print('add(2,2) is',using_reload_one.add(2,2))
using_reload_one=__import__('using_reload_two')
print('add(2,2) is',using_reload_one.add(2,2))
