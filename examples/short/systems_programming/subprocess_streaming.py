#!/usr/bin/python3

"""
This is an example of how to use the subprocess module for streaming

	Mark Veltzer <mark@veltzer.net>
"""

import subprocess

p=subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE)
for line in p.stdout:
	print(line.decode().rstrip())
