#!/usr/bin/python3

'''
This is an example of how to read XML in python using the built in
xml.etree module

	Mark Veltzer <mark@veltzer.net>
'''

import xml.etree.ElementTree # for ElementTree

mydoc=xml.etree.ElementTree.ElementTree(file='tst.xml')
for e in mydoc.findall('.//bar'):
	print(e.get('title'))
