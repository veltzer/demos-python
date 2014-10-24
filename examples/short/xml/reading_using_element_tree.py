#!/usr/bin/python3

'''
This is an example of how to read XML in python using the built in
xml.etree module
'''

import xml.etree.ElementTree # for ElementTree
import io # for StringIO

data='''
<root>
	<foo>
		<bar title='this is the text you are looking for'>
			bar content
		</bar>
	</foo>
</root>
'''

file=io.StringIO(data)

mydoc=xml.etree.ElementTree.ElementTree(file=file)
for e in mydoc.findall('.//bar'):
	print(e.get('title'))
