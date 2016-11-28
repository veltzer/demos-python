#!/usr/bin/python3

"""
Example of how to use the 'csv' module to write csv files
"""

import csv  # for writer

data = [
    ['first, element', 5, ],
    ['second, element', 7, ],
]
with open('/tmp/output.csv', 'w') as csvfile:
    w = csv.writer(csvfile)
    for d in data:
        w.writerow(d)
