"""
solution1.py
"""

import functools
import os
import sys

outfile = "/tmp/out.txt"


def with_output_to_outfile(f):
    """Decorate f to run with stdout redirected to [outfile].

    The file is opened for appending each time f will be called and
    closed when it returns.
    """

    @functools.wraps(f)
    def decorated_f(*args, **kw):
        old_stdout = sys.stdout
        # pylint: disable=consider-using-with
        new_stdout = sys.stdout = open(outfile, "a")
        try:
            return f(*args, **kw)
        finally:
            sys.stdout = old_stdout
            new_stdout.close()

    return decorated_f


@with_output_to_outfile
def hello(name):
    print(f"Hello, {name}!")


def main():
    # Running this will destroy [outfile]!
    # make sure file is empty
    with open(outfile, "w"):
        pass
    # test
    print("This should output nothing:")
    hello("Fred")
    hello("Barney")
    print("The file now contains this:")
    with open(outfile) as f:
        print(f.read())
    # clean up
    os.remove(outfile)


main()
