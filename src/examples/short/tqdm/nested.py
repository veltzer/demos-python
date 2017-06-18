#!/usr/bin/python3

"""
This is a basic example of how to use tqdm.

References:
- https://pypi.python.org/pypi/tqdm
"""

import tqdm
import time

for i in tqdm.tqdm(range(1000)):
    time.sleep(1)
    for i in tqdm.tqdm(range(1000)):
        time.sleep(0.001)
