#!/usr/bin/python3

'''
This is a basic logging example

The idea of passing __name__ to the logger
is that you can turn logs on and off from certain modules.
'''

import logging # for getLogger

logger=logging.getLogger(__name__)
logger.warning("this is a warning"+__name__)
