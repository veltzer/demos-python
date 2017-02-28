#!/usr/bin/python3

"""
This example shows how to remove the last character from a string

References:
- http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python
"""

s = "hello\n\n\t\n"

print("s.strip() is [{}]".format(s.rstrip()))
print("s.strip('\\n') is [{}]".format(s.rstrip("\n")))
