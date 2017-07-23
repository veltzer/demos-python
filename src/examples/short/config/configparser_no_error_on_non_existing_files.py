#!/usr/bin/env python

"""
This is an example that shows that ConfigParser does NOT complain about
reading files which don't exist.
Quite stupid.
"""

import os.path
import configparser

c = configparser.ConfigParser()
c.read('nonexit.ini')
