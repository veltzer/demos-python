#!/usr/bin/python3

'''
This example only captures stdout

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
'''

import subprocess  # for Popen, PIPE,
import sys  # for argv, stderr, exit

if len(sys.argv) < 2:
    print('must supply process to run and arguments for it', file=sys.stderr)
    sys.exit(1)

pr = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE, shell=False)
for line in pr.stdout:
    line = line.decode()
    print('got line [{0}]'.format(line.rstrip()))
