#!/usr/bin/python3

"""
This example will show how to wrap one io object with another.

TODO:
- write this example
"""

import io  # for TextIOWrapper
import sys  # for stdin

print(sys.stdout.detach())
f = io.TextIOWrapper(sys.stdin.detach())

for line in f:
    print(line)
