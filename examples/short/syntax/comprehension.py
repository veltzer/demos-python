#!/usr/bin/python3

'''
Exapmles of various types of comprehensions.
'''

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

# dictionaries
print({ 2:3,4:5 })
print({ x:x**2 for x in range(10) })

d={'mark':'veltzer', 'shay':'sarid'}
print(dict((y,x) for x,y in d.items()))
