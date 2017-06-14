#!/usr/bin/python3

"""
This is how to use tqdm when you know number of iterations.

References:
- https://pypi.python.org/pypi/tqdm
"""

import tqdm
import random

limit = 100000000
counter = 0
with tqdm.tqdm(total=limit) as pbar:
    while True:
        r = random.randrange(0, 100)
        counter += r
        if counter > limit:
            break
        pbar.update(r)

# and without the 'with' syntax:
pbar = tqdm.tqdm(total=limit)
counter = 0
while True:
    r = random.randrange(0, 100)
    pbar.update(r)
    counter += r
    if counter > limit:
        break
pbar.close()
