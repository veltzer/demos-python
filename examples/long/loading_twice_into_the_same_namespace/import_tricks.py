#!/usr/bin/python3

'''
This example shows how to use the 'imp' module to do double importing of content
into the same namespace
'''

import imp

imp.load_source('config','myfolder/mymod.py')
imp.load_source('config','myotherfolder/mymod2.py')
import config

''' another version
config=imp.load_source('config','myfolder/mymod.py')
imp.load_source('config','myotherfolder/mymod2.py')
'''
for var in config.__dict__:
	if not var.startswith('__'):
		print(var,config.__dict__[var])
