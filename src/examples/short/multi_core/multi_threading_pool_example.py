#!/usr/bin/python3

"""
This example shows how to use a multiprocessing pool
"""

import multiprocessing  # for cpu_count
import multiprocessing.pool  # for ThreadPool
import time  # for sleep

def sleep_a_little(num):
    print('before', num)
    time.sleep(1)
    print('after', num)

pool = multiprocessing.pool.ThreadPool(multiprocessing.cpu_count())
for i in range(10):
    pool.apply_async(sleep_a_little, [i])
pool.close()
pool.join()
