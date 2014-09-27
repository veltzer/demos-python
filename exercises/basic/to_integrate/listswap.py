#!/usr/bin/python3

size=raw_input('please enter a list size :')
size=int(size)
l=range(0,size)
for number in range(0,size) :
	num=raw_input('please enter a number '+str(number)+' :')
	num=int(num)
	l[number]=num
for number in range(0,size) :
	if number/2==0 :
		temp=l[number]
		l[number]=l[number+1]
		l[number+1]=temp
	pass
print(l)
