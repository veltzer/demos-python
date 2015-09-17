#!/usr/bin/python3

g = (x ** 2 for x in range(5))

over = False
while not over:
    try:
        # x=g.__next__()
        x = g.send(None)
        print(x)
    except StopIteration:
        over = True
g.close()
