#!/usr/bin/python

'''
Example of timing python code

	Mark Veltzer <mark@veltzer.net>
'''

import time # for time, sleep

time_before=time.time()
time.sleep(2)
time_after=time.time()
print('time taken: {0:.3f} seconds'.format(time_after-time_before))
