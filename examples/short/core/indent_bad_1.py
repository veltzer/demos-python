#!/usr/bin/python

"""
This example shows that python is strict about indentation and
will fail the compilation/running if the code is not strictly
indented.

	Mark Veltzer <mark@veltzer.net>
"""

x=[1,2,3]
for y in x:
 if y==2:
 	print(y)
  print(y)
