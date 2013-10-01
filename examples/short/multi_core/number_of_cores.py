#!/usr/bin/python3

"""
Getting the number of cores via python

	Mark Veltzer <mark@veltzer.net>
"""

import multiprocessing

print(multiprocessing.cpu_count())
