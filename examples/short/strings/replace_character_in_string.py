#!/usr/bin/python3

'''
These are examples of replacing a character or characters in strings.
'''

s='a.b.c'
print('-'.join(s.split('.')))
print(s.translate({ord('.'):'-'}))
