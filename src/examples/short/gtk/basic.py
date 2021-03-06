"""
A minimal gtk application demo.
"""

import signal

import gi

from gi.repository import Gtk
gi.require_version('Gtk', '3.0')


def clicked_callback(button):
    button.set_label('Hello World! ' + str(button.num))
    button.num += 1


def quit_callback(_window, _event):
    Gtk.main_quit()


b = Gtk.Button('Click me')  # create a button
b.num = 0  # attache some data to it
b.connect('clicked', clicked_callback)  # attach it to the callback

w = Gtk.Window()  # create a new window
w.add(b)  # put it inside the window
w.connect('delete-event', quit_callback)
w.show_all()  # must do this in GTK

signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()  # main loop. Will only quit if you call 'gtk.main_quit()'
