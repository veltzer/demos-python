#!/usr/bin/python

"""
This example shows how to call popen and get the return text.

	Mark Veltzer <mark@veltzer.net>
"""

import os

(pin,pout)=os.popen2(["ls","-l"])
for number, line in enumerate(pout):
	print(number, line)
