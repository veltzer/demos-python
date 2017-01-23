#!/usr/bin/python3

"""
This example shows how to approximate the <> operator of perl
in python.

Reminder: the <> operator (or as it's called diamond) reads
all line seither specified on the command line or from standard input.

References:
- https://mail.python.org/pipermail/tutor/2005-September/041607.html
"""

import sys

def diamond_lines():
    if len(sys.argv)==1:
        for line in sys.stdin.readlines():
            yield line
    else:
        for filename in sys.argv[1:]:
            with open(filename, 'rt') as file_handle:
                for line in file_handle:
                    yield line

for line in diamond_lines():
    print(line, end='')
