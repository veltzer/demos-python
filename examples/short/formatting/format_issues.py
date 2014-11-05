#!/usr/bin/python3

'''
This example explores issues that one may have with formatting.

Notes:
- if you want to write any string you like you need to use double
curly braces.
'''

try:
	s='''{this will not work} {0}'''.format('mark')
	print(s)
except Exception as e:
	print('yes, got an exception', e)

s='''{{this will work}} {0}'''.format('mark')
print(s)
