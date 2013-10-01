import sys
print "hello from the module itself"
def printit():
	print vars()
	print __name__
	print sys.modules[__name__]
	print sys.modules[__name__].__dict__
	#print __module__
