#!/usr/bin/python3

'''
Getting the number of cores via python
'''

import multiprocessing # for cpu_count

print(multiprocessing.cpu_count())
