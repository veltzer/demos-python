#!/usr/bin/python3

"""
This is how you want to use the logging module in a small script.

The key is the logging.basicConfig method to setup the config
for basic usage.

The problem with this example is that you set your own logging
level which is contrary to logging philosophy. You shuld not
set your own logging level.
"""

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.warning("this is a warning message %d", 1)
logger.debug("this is a debug message")
