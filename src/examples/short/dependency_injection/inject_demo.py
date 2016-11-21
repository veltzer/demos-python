#!/usr/bin/python3

'''
This is a demo of using the inject framework for python.

References:
- https://pypi.python.org/pypi/Inject/3.1.1
'''

import inject  # for configure, param

@inject.params(myvar=list)
def doit(myvar):
    print(myvar)

def configure(binder):  # type: inject.Binder
    binder.bind(list, [1,2,3])
inject.configure(config=configure)

doit()
