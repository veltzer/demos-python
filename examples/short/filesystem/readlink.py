#!/usr/bin/python3

'''
This is an example of how to read a symbolic link in python.
the API is os.readlink()
Notice that if you read the target of the symlink you still have
to fix it to find the *real* file that it is pointing to.

	Mark Veltzer <mark@veltzer.net>
'''
import os # for readlink 
import os.path # for islink, split, abspath, join, isabs

'''
this is a file name which is a symbolic name on most linux
systems...
'''
link='/etc/resolv.conf'
(link_folder,link_file)=os.path.split(link)
if os.path.islink(link):
	link_target=os.readlink(link)
	if os.path.isabs(link_target):
		real_link_target=os.path.abspath(link_target)
	else:
		real_link_target=os.path.abspath(os.path.join(link_folder, link_target))
	print(link_target)
	print(real_link_target)
else:
	raise ValueError('this file you gave [{0}] is not a symbolic link...'.format(link))
