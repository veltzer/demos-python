#!/usr/bin/python3

'''
example of how to convert the output of date(1) on the command line
to mysql type dates.
'''

import subprocess # for check_output
import datetime # for strptime

def date_to_mysql(output):
	format='%a %b %d %H:%M:%S %Z %Y'
	d=datetime.datetime.strptime(output, format)
	#print('d is [{0}]'.format(d))
	return d

output=subprocess.check_output('date').decode().strip()
print('output is [{0}]'.format(output))
d=date_to_mysql(output)
print('d is [{0}]'.format(d))
