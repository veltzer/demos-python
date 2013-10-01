#!/usr/bin/python

"""
This example shows how to use the "u" prefix to strings and the \u escape in strings to create
multi lingual strings. All in all its better not to do all of this and keep multi lingual strings
out of the code and put it in some external source (database,config file,...).

	Mark Veltzer <mark@veltzer.net>
"""

from __future__ import print_function

print(u"\u05d4\u05d9")
