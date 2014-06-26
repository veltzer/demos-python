#!/usr/bin/python3

"""
An example of an application sending an email.

	Mark Veltzer <mark@veltzer.net>
"""

import smtplib
import email.mime.text
import configparser
import os
import sys

def send_email():
	debug=False
	config=configparser.ConfigParser()
	config.read(["myworld.cfg"])
	p_subject=config.get("email","subject")
	p_from=config.get("email","from")
	p_to=config.get("email","to").split(",")
	p_smtp_host=config.get("email","smtp_host")
	p_content=config.get("email","content")
	p_user=config.get("email","user")
	p_password=config.get("email","password")
	p_debug=bool(config.get("email","debug"))
	p_usetls=bool(config.get("email","usetls"))
	#p_nonexist=config.get("email","nonexist")
	if(debug):
		#output the entire config
		config.write(sys.stdout)
		p_debug=True
	# build the message...
	msg=email.mime.text.MIMEText(p_content)
	msg["Subject"]=p_subject
	msg["From"]=p_from
	# Send the message via our own SMTP server,but dont include the # envelope header.
	server=smtplib.SMTP(p_smtp_host)
	if(p_debug):
		server.set_debuglevel(1)
	if(p_usetls):
		server.starttls()
	server.login(p_user,p_password)
	server.sendmail(p_from,p_to,msg.as_string())
	server.quit()

if __name__=="__main__":
	send_email()
