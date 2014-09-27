#!/usr/bin/python3

import sys, functools

def with_output_to_out_txt(f):
	'''Decorate f to run with stdout redirected to 'out.txt'.

	The file is opened for appending each time f will be called and
	closed when it returns.
	'''
	@functools.wraps(f)
	def decorated_f(*args, **kw):
		old_stdout=sys.stdout
		new_stdout=sys.stdout=open('out.txt', 'a')
		try:
			return f(*args, **kw)
		finally:
			sys.stdout=old_stdout
			new_stdout.close()
	return decorated_f

@with_output_to_out_txt
def hello(name):
	print('Hello, {0}!'.format(name))

# Running this will destroy 'out.txt' in the current dir!

if __name__=='__main__':
	import os
	# make sure file is empty
	open('out.txt', 'w').close()
	# test
	print('This should output nothing:')
	hello('Fred')
	hello('Barney')
	print('The file now contains this:')
	print(open('out.txt').read())
	# clean up
	os.remove('out.txt')
