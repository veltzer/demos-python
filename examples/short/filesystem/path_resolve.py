#!/usr/bin/python3

"""
This is an example of how to resolve a path in python

	Mark Veltzer <mark@veltzer.net>
"""
import os # for .path.join, .walk
import re # for .compile,.finditer
import sys # for .argv

if len(sys.argv)<2:
	raise ValueError("plase pass regexp")
c=re.compile(sys.argv[1])

for root,dirs,files in os.walk('.'):
	for file in files:
		full=os.path.join(root,file)
		for num,line in enumerate(open(full)):
			line=line[:-1]
			for x in c.finditer(line):
				print("{0},{1}: {2}".format(full,num,line))
