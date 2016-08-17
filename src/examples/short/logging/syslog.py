#!/usr/bin/python3

'''
This is an example of how to log to syslogd
'''

import logging # for getLogger
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
my_logger.addHandler(handler)

my_logger.debug('this is debug')
my_logger.critical('this is critical')
