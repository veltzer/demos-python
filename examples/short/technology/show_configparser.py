#!/usr/bin/python3

"""
This is an example of how to use pythons built-in configparser.

	Mark Veltzer <mark@veltzer.net>
"""
import configparser
import os.path

inifile=os.path.expanduser('~/.demo.ini')
if os.path.isfile(inifile):
	print('inifile exists, reading it')
	config=configparser.ConfigParser()
	config.read(inifile)
	myint=config.getint('mysection','myint')
	mybool=config.getboolean('mysection','mybool')
	myfloat=config.getfloat('mysection','myfloat')
	print('myint is {myint}'.format(**vars()))
	print('mybool is {mybool}'.format(**vars()))
	print('myfloat is {myfloat}'.format(**vars()))
else:
	print('inifile did not exist, writing it for the first time. find it in {inifile}'.format(**vars()))
	config=configparser.ConfigParser()
	config.add_section('mysection')
	config.set('mysection','myint',str(15))
	config.set('mysection','mybool',str(True))
	config.set('mysection','myfloat',str(3.14))
	with open(inifile, 'wb') as configfile:
		config.write(configfile)
