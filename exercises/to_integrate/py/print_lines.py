#!/usr/bin/python3

for line in open('/etc/passwd'):
	print('line is',line.rstrip())
