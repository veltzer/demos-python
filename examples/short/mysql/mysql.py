#!/usr/bin/python

from __future__ import print_function
import MySQLdb # for .connect
import sys # for .exit

try:
	conn=MySQLdb.connect(
		host='localhost',
		port=3306,
		user='root',
		passwd='root',
		db='mysql',
	)
	print('conn is',conn)
	with conn:
		cur=conn.cursor()
		cur.execute("SELECT VERSION()")
		data=cur.fetchone()
		print("Database version : {0}".format(data))
except MySQLdb.Error, e:
	print("Error {0}: {1}".format(*e))
	sys.exit(1)
