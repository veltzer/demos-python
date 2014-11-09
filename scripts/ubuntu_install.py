#!/usr/bin/python3

'''
this script will install all the required packages that you need on
ubuntu to compile and work with this package.
'''

import subprocess # for check_call

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
	'python3-progressbar',
	'python-networkx-doc', # tool to create, manipulate and study complex networks - documentation
	'python3-networkx', # tool to create, manipulate and study complex networks (Python3)
	'python3-pygraph', # library for working with graphs in Python (Python3)
	'python-yapsy', # simple plugin system for Python applications
	'python-yapsy-doc', # simple plugin system for Python applications - doc
	'python3-yapsy', # simple plugin system for Python3 applications
	'python3-pygments', # for syntaxh highlighting

	# sphinx
	'python3-sphinx', # documentation generator for Python projects (implemented in Python 3)
	'python3-sphinx-paramlinks', # allows param links in Sphinx function/method descriptions to be linkable
	'python3-sphinxcontrib.programoutput', # insert the output of arbitrary commands into documents Python 3.x
	'python3-sphinxcontrib.spelling', # Sphinx "spelling" extension (Python 3)
	'python3-sphinxcontrib.youtube', # Sphinx "YouTube" extension

	# from my own repo
	'templar',
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)
