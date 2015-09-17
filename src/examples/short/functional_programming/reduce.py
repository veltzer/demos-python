#!/usr/bin/python3

'''
A basic python functional 'reduce' example
'''

import functools # for reduce

def add(x, y):
    return x + y


print(functools.reduce(add, range(100)))
