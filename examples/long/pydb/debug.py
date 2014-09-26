#!/usr/bin/python

'''
This is an example of a simple python application
that you can use to debug with pydb.
'''

def calc():
	i=0
	sum=0
	while True:
		sum=sum+i
		i=i+1

if __name__=='__main__':
	calc()
