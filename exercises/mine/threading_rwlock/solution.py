#!/usr/bin/python

class RWL:
	def __init__(self):
		self._writersWaiting=0
		self._readersWaiting=0
		self._writersInside=0
		self._readersInside=0
		self.c=threading.Condition()
	def ReaderEnter(self):
		with self.c:
			self._readersWaiting++
			while self._writersInside:
				self.c.wait()
			self._readersWaiting--
			self._readersInside++
	def ReaderLeave(self):
		with self.c:
			self._readersInside--
			#self.c.notifyAll()
			if self._readersInside==0:
				self.c.notify()
	def WriterEnter(self):
		with self.c:
			self._writersWaiting++
			while self._readersInside || self._writersInside:
				self.c.wait()
			self._writersWaiting--
			self._writerInside++
	def WriterLeave(self):
		with self.c:
			self._writerInside--
			self.c.notifyAll()
