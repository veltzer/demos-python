#!/usr/bin/python3

'''
Example of disassembling a python function
'''

import dis # for dis
import inspect # for getsourcelines

def add(a, b):
	return a+b

print(dis.dis(add))
print(inspect.getsourcelines(add))
