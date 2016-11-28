#!/usr/bin/python3

"""
This is a demo of using the inject framework for python.

References:
- https://pypi.python.org/pypi/Inject/3.1.1
"""

import inject


@inject.params(var=list)
def doit(var):
    print(var)


def configure(binder):  # type: (inject.binder) -> None
    binder.bind(list, [1, 2, 3])


inject.configure(config=configure)

doit()
