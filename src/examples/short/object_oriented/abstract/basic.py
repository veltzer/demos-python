#!/usr/bin/python3

"""
This is an example of how to make an abstract class in python

Notes:
- As can be seen from the example a class which only hooks
to the __metaclass__ of abc.ABCMeta CAN BE INSTANTIATED.
- only if the class has at least one abstract method then
it cannot be instantiated (second example).
- in python2 the syntax for this was different:
    class A:
        __metaclass__ = abc.ABCMeta
"""

import abc


class A(metaclass=abc.ABCMeta):
    pass


class B(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def foo(self):
        pass


class C(B):
    def foo(self):
        pass


a = A()
assert isinstance(a, A)
try:
    b = B()
except Exception as e:
    print('yes, got exception [{0}]...'.format(str(e)))
c = C()
assert isinstance(c, C)
assert issubclass(C, B)
