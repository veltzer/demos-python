mylist=[]
x=100
while x>0:
	mylist.append(x)
	x-=2
# now we have all the numbers in 'mylist'
mysum=0
for x in mylist:
	mysum+=x
print mysum
