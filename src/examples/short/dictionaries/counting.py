#!/usr/bin/python3

'''
This example shows how to count using a dictionary
'''

colors = [
    'red',
    'green',
    'red',
    'blue',
    'green',
    'red',
]

# the simple way
d={}
for color in colors:
    if color not in d:
        d[color]=0
    d[color]+=1
print(d)

# shorter code
d={}
for color in colors:
    d[color]=d.get(color, 0)+1
print(d)
