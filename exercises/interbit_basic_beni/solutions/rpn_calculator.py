#!/usr/bin/python

# This magic line fixes 3/2 to return 1.5 and not 1.
# You always want it in any Python program using division.
# (When you do want 1, use the 3 // 2 operator.)
from __future__ import division

# A function for each operation. You'll see below why I do this.
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
# (BTW, the `operator` module is packed with function like these.)

# Functions are objects like anything else, we can stick them in a dict!
operators={'+': add, '-': sub, '*': mul, '/': div}

def rpn_calc(expression):
	stack=[]
	print stack
	for word in expression.split():
		print word
		if word not in operators:
			stack.append(float(word))
		else:
			b=stack.pop()
			a=stack.pop()
			# Instead of writing many if..elif... cases, just call
			# whatever function the dict gave us.
			stack.append(operators[word](a, b))
		print stack

rpn_calc(" ".join(["2","2","+","5","*"]))
