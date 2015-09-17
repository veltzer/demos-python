#!/usr/bin/python2

num = int(raw_input('Please enter number of elements: '))
list = []
for x in xrange(num):
    current = int(raw_input('Please enter element' + str(x) + ': '))
    list.append(current)
for x in xrange(0, num - 1, 2):
    [list[x], list[x + 1]] = [list[x + 1], list[x]]
print(list)
