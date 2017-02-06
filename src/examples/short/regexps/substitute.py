#!/usr/bin/python3

"""
Example of how to substitute parts of a string using regular expressions.
"""

import re  # for sub

print(re.sub(r'abc', 'z', 'abcdefghijkabcde'))
