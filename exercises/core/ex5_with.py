#!/usr/bin/python3

import sys, contextlib

@contextlib.contextmanager
def redirect_output_to(fname):
	'''Context manager to run with stdout redirected to fname.
	The file is opened for appending and closed when the block
	finishes.
	'''
	old_stdout=sys.stdout
	new_stdout=sys.stdout=open(fname, 'a')
	try:
		yield
	finally:
		sys.stdout=old_stdout
		new_stdout.close()


# Running this will destroy 'out3.txt' in the current dir!

if __name__=='__main__':
	import os
	# make sure file is empty
	open('out3.txt', 'w').close()
	# test
	print('This should output nothing:')
	for name in ['Fred', 'Barney']:
		with redirect_output_to('out3.txt'):
			print('Hello, {0}!'.format(name))
	print('The file now contains this:')
	print(open('out3.txt').read())
	# clean up
	os.remove('out3.txt')
