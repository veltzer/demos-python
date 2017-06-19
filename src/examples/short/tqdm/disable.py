#!/usr/bin/python3

"""
this is how to disable tqdm
"""

import tqdm
import time

for i in tqdm.tqdm(range(1000), disable=True):
    time.sleep(1)
