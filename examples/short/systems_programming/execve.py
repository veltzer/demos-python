#!/usr/bin/python

"""
This is an example of how to use execve in python...

	Mark Veltzer <mark@veltzer.net>
"""
import os

#os.system("ls -l")
os.execl("/bin/ls","-l")
print("Where did I go ?!?")
