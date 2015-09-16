#!/usr/bin/python3

def min_max_avg(list):
	min=list[0]
	max=list[0]
	sum=list[0]
	for i in xrange(1,len(list)):
		x=list[i]
		if x<min:
			min=x
		if x>max:
			max=x
		sum+=x
	return min,max,sum/len(list)

print(min_max_avg(xrange(0,100000)))
