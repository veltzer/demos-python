#!/usr/bin/python2

'''
Usage: get_person.py 'personID'

NOTES:
- this script is python2 on purpose because the imdb module is currently only available for python2 in ubuntu.
'''

from __future__ import print_function
import sys # for exit, argv
import imdb # for IMDb

if len(sys.argv)!=2:
	print('{0}: usage: {0} [personID]'.format(sys.argv[0]))
	print('{0}: usage: {0} 0124930'.format(sys.argv[0]))
	sys.exit(1)

personID=sys.argv[1]
connection=imdb.IMDb()

person=connection.get_person(personID)

for k in person.keys():
	print('[{0}],[{1}]'.format(k, person[k]))
