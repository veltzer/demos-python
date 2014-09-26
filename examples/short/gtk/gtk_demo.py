#!/usr/bin/python

'''
A minimal gtk application demo.
'''

import gtk # for Button, Window, main

def callback(b):
	b.set_label('Hello World!'+str(b.num))
	b.num+=1

b=gtk.Button('Click me') # create a button
b.num=0 # attache some data to it
b.connect('clicked',callback) # attach it to the callback
w=gtk.Window() # create a new window
w.add(b) # put it inside the window
w.show_all() # must do this in GTK
gtk.main() # there's no way out of here
