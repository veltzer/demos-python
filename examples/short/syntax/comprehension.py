#!/usr/bin/python

"""
Exapmles of various types of comprehensions.

	Mark Veltzer <mark@veltzer.net>
"""

l=[x*y for x in range(10) for y in range(10)]
print(l)

new_list=[]
for x in range(10):
	for y in range(10):
		new_list.append(x*y)
print(new_list)

tup_list=[]
for x in range(10):
	for y in range(10):
		tup_list.append((x,y))
print(map(lambda t: t[0]*t[1],tup_list))

print({ x*2 for x in range(10) })
print({ 2,3,4 })
print({ 2:3,4:5 })
print({ x:x**2 for x in range(10) })
