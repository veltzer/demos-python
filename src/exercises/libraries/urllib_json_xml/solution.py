#!/usr/bin/python3

import urllib2
import json
import xml.etree.cElementTree as ET

URL = 'http://ws.geonames.org/hierarchyJSON?geonameId=2657896'
places = json.loads(urllib2.urlopen(URL).read())['geonames']

root = last = ET.Element('place', name=places[0]['name'])
for place in places[1:]:
    last = ET.SubElement(last, 'place', name=place['name'])

print(ET.tostring(root))
