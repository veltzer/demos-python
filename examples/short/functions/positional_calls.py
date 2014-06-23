#!/usr/bin/python

from __future__ import print_function

def add(x,y):
	return x+y
def sub(x,y):
	return x-y

name=raw_input("give me the name off the function ")
num=int(raw_input("how many arguments do you want to pass to the function ? "))
l=[]
for i in xrange(num):
	a=raw_input("give me another argument ")
	l.append(a)
print((vars()[name])(*l))
