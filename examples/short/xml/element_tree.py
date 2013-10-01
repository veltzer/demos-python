#!/usr/bin/python3

import xml.etree.ElementTree

mydoc=xml.etree.ElementTree.ElementTree(file='tst.xml')
for e in mydoc.findall('.//bar'):
	print(e.get('title'))
