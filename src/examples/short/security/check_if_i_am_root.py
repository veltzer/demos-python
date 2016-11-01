#!/usr/bin/python3

'''
This example shows how to check if you are root in python.

References:
- http://www.servercobra.com/python-check-if-script-is-run-as-root/
'''

import os # for geteuid
import sys # for exit

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')
