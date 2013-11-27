#!/usr/bin/python

def swap_lists(l1,l2):
	for i in xrange(len(l1)):
		l1[i],l2[i]=l2[i],l1[i]

list1=["a","b","c"]
list2=[7,8,9]
swap_lists(list1,list2)
print list1, list2
