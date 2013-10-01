#!/usr/bin/env python

import sys
import pygtk
import gtk
import gtk.glade

"""
TODO: check why this does not work!
"""

class HellowWorldGTK:
	"""This is an Hello World GTK application"""
	def __init__(self):
		#Set the Glade file
		self.gladefile="project.glade"
		#self.gladefile="myproject.glade"
		self.wTree=gtk.glade.XML(self.gladefile)
		#Get the Main Window, and connect the "destroy" event
		self.window=self.wTree.get_widget("window1")
		if (self.window):
			self.window.connect("destroy", gtk.main_quit)

if __name__=="__main__":
	hwg=HellowWorldGTK()
	gtk.main()
