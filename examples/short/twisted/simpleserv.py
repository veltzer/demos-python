#!/usr/bin/python

"""
A simple twisted server doing echo on two ports.

	Mark Veltzer <mark@veltzer.net>
"""

from twisted.internet import reactor,protocol

class Echo(protocol.Protocol):
	"""This is just about the simplest possible protocol"""
	def dataReceived(self,data):
		"As soon as any data is received,write it back."
		self.transport.write(data)

factory=protocol.ServerFactory()
factory.protocol=Echo

"""This runs the protocol on port 8000"""
reactor.listenTCP(8000,factory)
"""And again on port 8002"""
reactor.listenTCP(8002,factory)
reactor.run()
