#!/usr/bin/python3

'''
A simple example of how to get or set environment variables from python
'''

import os # for environ

print(os.environ['USER'])
if 'HOSTNAME' in os.environ:
	print(os.environ['HOSTNAME'])
else:
	print('you dont have a HOSTNAME in your environment, it is probably just a shell variable')
for k, v in os.environ.items():
	print(k, v)
