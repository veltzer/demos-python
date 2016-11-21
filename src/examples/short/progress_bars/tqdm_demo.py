#!/usr/bin/python3

'''
This shows how to use tqdm as a progress bar

References:
- https://pypi.python.org/pypi/tqdm
'''

import tqdm
import time

for i in tqdm.tqdm(range(1000)):
    time.sleep(1)
