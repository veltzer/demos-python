#!/usr/bin/python

"""
This is a basic demo of how to use the ctypes python library to load
a library and use it.

	Mark Veltzer <mark@veltzer.net>
"""

import ctypes
libc=ctypes.cdll.LoadLibrary("libc.so.6")
print(libc.time(None))
