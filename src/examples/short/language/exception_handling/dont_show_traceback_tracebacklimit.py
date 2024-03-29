"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

This example shows how to do this using sys.tracebacklimit.

This method is not the best since it still shows information you may not want
when multiple exceptions are raised.

References:
- http://stackoverflow.com/questions/17784849/
in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import sys


def do_error():
    try:
        raise ValueError("core")
    except ValueError as e:
        raise ValueError("outer") from e


sys.tracebacklimit = 0
do_error()
