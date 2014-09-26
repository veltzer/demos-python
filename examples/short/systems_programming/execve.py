#!/usr/bin/python

'''
This is an example of how to use execve in python...
'''

import os # for execl

os.execl('/bin/ls','-l')
print('Where did I go ?!?')
