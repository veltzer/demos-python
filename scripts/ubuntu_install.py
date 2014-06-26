#!/usr/bin/python

# this script will install all the required packages that you need on
# ubuntu to compile and work with this package.

import subprocess

packs=[
	'python3.4',
	'python3.4-doc',
	'pyqt4-dev-tools',
	'python-qt4',
	'python-qt4-sql',
	'python-qt4-dbus',
	'python3-pyqt4',
	'python3-dbus.mainloop.qt',
	'python-newt',
	'python3-newt',
	'python-dialog',
	'python-imdbpy',
	'python-mysql.connector',
	'python3-mysql.connector',
]

args=['sudo','apt-get','install']
args.extend(packs)
subprocess.check_call(args)
