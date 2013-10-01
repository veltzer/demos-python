#!/usr/bin/python3

"""
This is an example of the 'os.walk' API that allows one to traverse
a directory of files recursivly.
This is used to implement find(1)+grep(1) in just a few lines of python.

	Mark Veltzer <mark@veltzer.net>
"""
import os # for .path.join, .walk
import sys # for .argv

if len(sys.argv)<2:
	raise ValueError("plase pass root_folder")
root_folder=sys.argv[1]

for root,dirs,files in os.walk(root_folder):
	print(root)
	for cfile in files:
		full=os.path.join(root,cfile)
		print(full)
	for cdir in dirs:
		full=os.path.join(root,cdir)
		print(full)
