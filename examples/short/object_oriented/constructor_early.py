#!/usr/bin/python

'''
This example shows how to get out of a constructor early.
This is done via 'return None' or simply 'return' (which is the same).
'''

class Book:
	def __init__(self,price):
		self.__price=price
		#return None
		return
	def setPrice(self,val):
		self.__price=val
	def getPrice(self):
		return self.__price
	def printMe(self):
		print('printMe: price is',self.__price)

b=Book(50)
b.setPrice(60)
print(type(b))
print(dir(b))
b.printMe()
