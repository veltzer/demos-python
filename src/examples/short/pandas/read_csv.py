#!/usr/bin/python3

"""
A demo of how to load a csv file
"""

import pandas

df = pandas.read_csv("/etc/passwd", sep=":")
print(df)
