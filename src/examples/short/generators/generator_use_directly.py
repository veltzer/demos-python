#!/usr/bin/python3

"""
This is an example for how to use a generator directly and get all of it's values
throught the python API and not through the iterator abstraction (for loop).
"""

g = (x ** 2 for x in range(5))

print(dir(g))

over = False
while not over:
    try:
        x = g.__next__()
        # x = g.send(None)
        print(x)
    except StopIteration:
        over = True
g.close()
