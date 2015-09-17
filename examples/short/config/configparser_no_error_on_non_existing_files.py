#!/usr/bin/python3

'''
This is an example that shows that ConfigParser does NOT complain about
reading files which don't exist.
Quite stupid.
'''

import os.path  # for isfile
import configparser  # for ConfigParser

c = configparser.ConfigParser()
c.read('nonexit.ini')
