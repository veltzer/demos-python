#!/usr/bin/env python

"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

References:
- http://stackoverflow.com/questions/17784849/in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import sys


def do_error():
    try:
        raise ValueError('core')
    except Exception as e:
        raise ValueError('outer') from e


def excepthook(type, value, traceback):
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    while value.__cause__:
        value = value.__cause__
    print(value)


sys.excepthook = excepthook

do_error()
