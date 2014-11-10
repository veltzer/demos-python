#!/usr/bin/python3

'''
This is an example that shows how to calculate the relative paths of one path to the other.
'''

import os.path # for relpath

print(os.path.relpath('/etc/passwd', '/etc'))
