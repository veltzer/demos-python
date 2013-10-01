#!/usr/bin/python

"""
This is the right way to create a static method in python.
Wrap it using the 'staticmethod' function...
You can then call the method using the instance AND using
the class.

	Mark Veltzer <mark@veltzer.net>
"""
class Book:
	num=0
	def __init__(self,price):
		self.__price=price
		Book.num+=1
	def printit(self):
		print('price is',self.__price)
	def setPrice(self,newprice):
		self.__price=newprice
	def getNumBooks():
		return Book.num
	getNumBooks=staticmethod(getNumBooks)

b1=Book(14)
b2=Book(13)

print(Book.num)
print(b1.getNumBooks())
print(Book.getNumBooks())
