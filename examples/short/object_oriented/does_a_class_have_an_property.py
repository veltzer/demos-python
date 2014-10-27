#!/usr/bin/python3

'''
This is an exploration of how to find out if a class has a property
'''

class A(object):
	foo='foo'
	bar='bar'

	@classmethod
	def do_i_have_it(cls, prop):
		return prop in cls.__dict__

print(A.do_i_have_it('foo'))
print(A.do_i_have_it('bar'))
print(A.do_i_have_it('zoo'))
