#!/usr/bin/python3

'''
This example shows how to launch a process asynchoronously in python

References:
- http://stackoverflow.com/questions/636561/how-can-i-run-an-external-command-asynchronously-from-python
'''

import subprocess
import time  # for sleep

p = subprocess.Popen(['watch', 'ls']) # something long running
time.sleep(10)
p.terminate()
