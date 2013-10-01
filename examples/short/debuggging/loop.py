#!/usr/bin/python

"""
This is an example of debugging python with pdb.

	Mark Veltzer <mark@veltzer.net>
"""

def calc():
	i=0
	sum=0
	while True:
		sum=sum+i
		i=i+1

if __name__=="__main__":
	calc()
