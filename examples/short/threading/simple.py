#!/usr/bin/python3

'''
A very simple example of python threads

References:
http://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/
'''

import threading # for Thread
import time # for sleep

def myfunc(i):
	print('thread {0} is going to sleep...'.format(i))
	time.sleep(5)
	print('thread {0} is waking up...'.format(i))

threads=[]
for i in range(10):
	threads.append(threading.Thread(target=myfunc, args=(i,)))
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
