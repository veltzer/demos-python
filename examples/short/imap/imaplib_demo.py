#!/usr/bin/python

"""
This example shows how to use the imaplib module.
In this case I use it to access my gmail account, upload messages, download messages
and more.

		Mark Veltzer <mark@veltzer.net>
"""

import imaplib # for IMAP4_SSL
import ConfigParser # for ConfigParser
import os.path # for expanduser

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.pyimap.ini'))
opt_username = config.get('imap', 'username')
opt_password = config.get('imap', 'password')
opt_hostname = config.get('imap', 'hostname')

imap = imaplib.IMAP4_SSL(opt_hostname)
imap.login(opt_username, opt_password)
print(imap.capability())
print(imap.list())
imap.logout()
