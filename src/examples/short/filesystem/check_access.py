#!/usr/bin/python3

"""
This is an example of how to check access for different files.

NOTES:
- if a file does not exists os.access will return 'False'
on all types of access to it.
"""

import os

print(os.access('/etc/passwd', os.W_OK))
print(os.access('/etc/passwd', os.R_OK))
print(os.access('/tmp/doesnt_exist', os.R_OK))
print(os.access('/tmp/doesnt_exist', os.W_OK))
print(os.access('/tmp/doesnt_exist', os.X_OK))
