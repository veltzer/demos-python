#!/usr/bin/python3

'''
This is an example of the 'os.walk' API that allows one to traverse
a directory of files recursivly.
This is used to implement find(1)+grep(1) in just a few lines of python.

	Mark Veltzer <mark@veltzer.net>
'''
import os # for listdir
import sys # for arv

if len(sys.argv)<2:
	raise ValueError('please pass folder')
folder=sys.argv[1]

for file in os.listdir(folder):
	print(file)
