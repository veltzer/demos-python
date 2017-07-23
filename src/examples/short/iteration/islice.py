#!/usr/bin/env python

"""
This example shows how to use itertools.islice to cut down on the number
of iteration that a loop does...
"""

import sys
from itertools import islice

for i in islice(range(1000), sys.maxsize):
    print(i)
