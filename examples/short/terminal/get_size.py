#!/usr/bin/python

"""
A program that shows you how to get the size of the terminal.

	Mark Veltzer <mark@veltzer.net>
"""

import os # for popen, environ
import fcntl # for ioctl
import struct # for unpack, pack
import termios # for TIOCGWINSZ

def terminal_size1():
	h, w, hp, wp = struct.unpack('HHHH',
		fcntl.ioctl(0, termios.TIOCGWINSZ,
		struct.pack('HHHH', 0, 0, 0, 0)),
	)
	return w, h
def terminal_size2():
	ret=os.popen('stty size', 'r').read().split()
	return (int(ret[1]), int(ret[0]))
def terminal_size3():
	x=int(os.popen('tput cols', 'r').read())
	y=int(os.popen('tput lines', 'r').read())
	return (x,y)
# this function does not work since LINES and COLUMNS are not exported
def terminal_size4():
	x=int(os.environ['LINES'])
	y=int(os.environ['COLUMNS'])
	return (x,y)
def terminal_size5():
	d=dict()
	for tc_entry in os.environ['TERMCAP'].split(':'):
		if tc_entry.find('#')!=-1:
			key, val=tc_entry.split('#')
			d[key]=val
	return (int(d['co']), int(d['li']))

print(terminal_size1())
print(terminal_size2())
print(terminal_size3())
#print(terminal_size4())
print(terminal_size5())
