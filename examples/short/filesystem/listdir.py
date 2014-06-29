#!/usr/bin/python3

'''
This is an example of how to use the os.listdir API
to get all the files in a specific folder.
This is more efficient than the glob module since it
does not support regular expressions of any kind and
is the right thing to use if you need ALL the files
in a folder

	Mark Veltzer <mark@veltzer.net>
'''
import os # for listdir
import sys # for arv

if len(sys.argv)<2:
	raise ValueError('please pass folder')
folder=sys.argv[1]

for file in os.listdir(folder):
	print(file)
