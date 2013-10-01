#!/usr/bin/python3

"""
This example shows how to shuffle a list in python

	Mark Veltzer <mark@veltzer.net>
"""

import random
# for deterministic behaviour
random.seed(7)
l=list(range(1,10))
random.shuffle(l)
print(l)
