#!/usr/bin/python3

'''
This is a "fast" singleton in that you pay for only in the first
call. All subsequent calls don't even have an 'if' statement in them...

We also compare the difference in speed between the variation with
the if statement and without.
'''

import time # for time
import sys # for exit

class A:
	def __init__(self):
		pass

Ainstance=None
def getAInstance():
	global Ainstance, getAInstance
	print('in here')
	if Ainstance is None:
		Ainstance=A()
	def getAInstanceFast():
		return Ainstance
	getAInstance=getAInstanceFast
	return Ainstance

A1=getAInstance()
A2=getAInstance()
print(type(A1))
print(type(A2))
print(A1)
print(A2)
if A1 is A2:
	print('yes,they are the same instance')

class B:
	def __init__(self):
		pass

Binstance=None
def getBInstance():
	global Binstance
	if Binstance is None:
		Binstance=B()
	return Binstance

B1=getBInstance()
B2=getBInstance()
print(type(B1))
print(type(B2))
print(B1)
print(B2)
if B1 is B2:
	print('yes,they are the same instance')

#sys.exit(0)

# now lets measure times
num=10000000
time_before=time.time()
for i in range(num):
	a=getAInstance()
time_after=time.time()
print('time for A: {0:.3f} seconds'.format(time_after-time_before))
time_before=time.time()
for i in range(num):
	b=getBInstance()
time_after=time.time()
print('time for B: {0:.3f} seconds'.format(time_after-time_before))
