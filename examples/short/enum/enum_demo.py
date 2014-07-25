#!/usr/bin/python3

'''
Example of an enum in python3

	Mark Veltzer <mark@veltzer.net>
'''

import enum # for Enum

class Event(enum.Enum):
	nodepreadd=1
	nodepostadd=2
	nodepredel=3
	nodepostdel=4
	edgepreadd=5
	edgepostadd=6
	edgepredel=7
	edgepostdel=8
	nodeprebuild=9
	nodepostbuild=10

def is_enum(x):
	if isinstance(x, Event):
		print('yes')
	else:
		print('no')

is_enum(7)
is_enum(Event.edgepredel)

print(Event.edgepredel)
print(dir(Event.edgepredel))
print("name is [{name}] and type is [{type}]".format(
	name=Event.edgepredel.name,
	type=type(Event.edgepredel.name),
))
print("value is [{value}] and type is [{type}]".format(
	value=Event.edgepredel.value,
	type=type(Event.edgepredel.value),
))
