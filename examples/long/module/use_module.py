#!/usr/bin/python

# a basic hello world program...
from __future__ import print_function
import outer.inner.mod

print("hello from the module user")

outer.inner.mod.printit()
