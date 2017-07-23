#!/usr/bin/env python

"""
These are examples of replacing a character or characters in strings.
"""

s = 'a.b.c'
print('-'.join(s.split('.')))
print(s.replace('.', '-'))
print(s.translate({ord('.'): '-'}))
