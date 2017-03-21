#!/usr/bin/python3

"""
This is an example of how to write a simple md5 sum function in python
"""

import hashlib  # for md5

def md5_string(s: str) -> str:
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

print(md5_string("hello"))
