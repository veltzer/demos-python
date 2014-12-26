#!/usr/bin/python3

'''
This example only captures stdout

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
'''

import sys # for argv, stderr, exit, wait, WIFEXISTED, WEXITSTATUS, WIFSTOPPED, WSTOPSIG, WIFSIGNALED, WTERMSIG
import pty # for fork
import os # for execv, fdopen, read

if len(sys.argv)<2:
	print('{0}: must supply process to run and arguments for it'.format(sys.argv[0]), file=sys.stderr)
	print('{0}: use it like this:'.format(sys.argv[0]))
	print('{0}: {0} ./write_to_any.py stdout stderr tty'.format(sys.argv[0]))
	sys.exit(1)

(pid, fd)=pty.fork()
if pid==0:
	os.execv(sys.argv[1], sys.argv[1:])
	print('execv didnt work', sys.stderr)
else:
	'''
	there are two options to write this code: low level (shown first) and high level (shown second).
	take your pick

	At the end of the loop we get an exception when the connection with the other side terminates.
	This is kinda ugly since strictly speaking this is not an error, but oh well.
	'''
	'''
	bufsize=1024
	buf=os.read(fd, bufsize)
	over=False
	while len(buf)>0 and not over:
		print('got line [{0}]'.format(buf.decode().rstrip()))
		try:
			buf=os.read(fd, bufsize)
		except OSError as e:
			over=True
	'''
	try:
		for line in os.fdopen(fd):
			print('got line [{0}]'.format(line.rstrip()))
	except OSError as e:
		#print(e)
		pass
	(pid,ret)=os.wait()
	if os.WIFEXITED(ret):
		print('process was signaled and signal was [{0}]'.format(os.WEXITSTATUS(ret)))
	if os.WIFSTOPPED(ret):
		print('process was signaled and signal was [{0}]'.format(os.WSTOPSIG(ret)))
	if os.WIFSIGNALED(ret):
		print('process was signaled and signal was [{0}]'.format(os.WTERMSIG(ret)))
