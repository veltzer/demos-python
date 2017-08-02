#!/usr/bin/env python

"""
This script shows how to detect which version of python you are running in.

References:
- http://sweetme.at/2013/10/21/how-to-detect-python-2-vs-3-in-your-python-script/
"""

import sys

if sys.version_info > (3, 0):
    print("you are in python 3")
else:
    print("you are in python 2")
