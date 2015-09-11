#!/usr/bin/python3

'''
This is a cheating example since it used the str.count() method.
'''

s=raw_input('Please enter a line of digits: ')
for i in range(10):
	print('{i} appeared {count} times in the text'.format(i=i,count=s.count(str(i))))
