import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa: E402

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show()
Gtk.main()
