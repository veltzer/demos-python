#!/usr/bin/python3

'''
AsyncNotifier example from tutorial

See: http://github.com/seb-m/pyinotify/wiki/Tutorial
'''

import asyncore # for loop
import pyinotify # for WatchManager, IN_DELETE, IN_CREATE, AsyncNotifier

folder='/tmp'

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print('Creating:', event.pathname)

    def process_IN_DELETE(self, event):
        print('Removing:', event.pathname)

wm = pyinotify.WatchManager()  # Watch Manager
notifier = pyinotify.AsyncNotifier(wm, EventHandler())
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events
wdd = wm.add_watch(folder, mask, rec=True)
print('watching [{0}] for changes...'.format(folder))

print('going into mainloop')
asyncore.loop()
