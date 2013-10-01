#!/usr/bin/python

def call_n_times(n,f,*args,**kwargs):
	for i in xrange(n):
		f(*args,**kwargs)

def print_string(s):
	print s
call_n_times(5,print_string,"mark")
