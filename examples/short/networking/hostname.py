#!/usr/bin/python3

'''
This example shows the various ways to get the host name in python.
'''

import socket # for gethostname
import platform # for node, uname
import os # for uname, getenv

print(socket.gethostname())
print(platform.node())
print(platform.uname()[1])
print(os.uname()[1])
print(os.getenv('HOSTNAME')) # HOSTNAME is not always an environment variables so this may not work
print(os.getenv('HOST')) # HOST is not always an environment variables so this may not work
print(socket.gethostbyaddr(socket.gethostname())[0])
print(socket.getfqdn())
