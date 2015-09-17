#!/usr/bin/python2

'''
This example shows how to call popen and get the return text.
'''

from __future__ import print_function
import os # for popen2

(pin,pout)=os.popen2(['./demo_process.py'], bufsize=1)
print(dir(pout))
for line in pout.readlines():
	print('line is', line, end='')
