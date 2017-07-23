#!/usr/bin/env python

"""
This example shows how to call popen and get the return text.
"""

import os

pout = os.popen('./demo_process.py', buffering=1)
for line in pout:
    print('line is', line, end='')
