#!/usr/bin/python3

'''
This is an example of how to writing XML in python using the built in
xml.etree module

The only problem with this is that xml.etree.ElementTree does not know how
to pretty output xml and so I do the corretion using xml.dom.minidom at
the bottom.
'''

import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys # for stdout

output_file='output.xml'

root=ET.Element('root')
doc=ET.SubElement(root, 'doc')

field1=ET.SubElement(doc, 'field1')
field1.set('name', 'name of field1')
field1.text='field 1 free text'

field1=ET.SubElement(doc, 'field2')
field1.set('name', 'name of field2')
field1.text='field 2 free text'

tree=ET.ElementTree(root)
#print(dir(tree))
#print(help(tree.write))
tree.write(output_file)

# lets fixup the xml by overwriting the file with the pretty version
xml=xml.dom.minidom.parse(output_file)
pretty_xml=xml.toprettyxml()
with open(output_file, 'w') as f:
	f.write(pretty_xml)
