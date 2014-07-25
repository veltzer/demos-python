#!/usr/bin/python3

"""
An example of how to use python3-progressbar
"""

import progressbar # for ProgressBar
import time # for sleep

pbar = progressbar.ProgressBar()
pbar.start()
for i in range(10):
	# do something
	time.sleep(1)
	pbar.update(i+1)
pbar.finish()
