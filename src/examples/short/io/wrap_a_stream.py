#!/usr/bin/python3

"""
This example will show how to wrap one io object with another.
"""

import io  # for TextIOWrapper
import sys  # for stdin
import itertools

filename = "/etc/passwd"

# default mode of open is "rt"
with open(filename, "rb") as file_handle:
    for line in itertools.islice(file_handle, 5):
        print(line)

with open(filename, "rb") as file_handle:
    wrapped = io.TextIOWrapper(file_handle)
    for line in itertools.islice(wrapped, 5):
        print(line, end='')
