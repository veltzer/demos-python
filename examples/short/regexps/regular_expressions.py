#!/usr/bin/python3

"""
This is a sample for using regular expressions in python

	Mark Veltzer <mark@veltzer.net>
"""
import re # for compile, finditer

c=re.compile('^\tfoobar (\d+)\n$')

# lets get the match object
m=c.match('\tfoobar 17\n')
if m:
	print('m.group() is [{g}]'.format(g=m.group()))
	print('m.group(1) is [{g}]'.format(g=m.group(1)))
else:
	print('no match')
