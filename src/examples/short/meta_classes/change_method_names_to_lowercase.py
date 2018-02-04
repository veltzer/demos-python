#!/usr/bin/env python

"""
This is an example of how to use meta classes to change all class methods to lowercase.
The most important things to remember about writing meta classes:
- override '__new__' when you want to override the class creation.
- override '__init__' when you want to intervene after class creation.

References:
- https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
"""
class MetaClass(type):
    def __new__(mcs, name, bases, cls_dict):
        new_dict = dict()
	for k, v in cls_dict.iteritems():
            new_dict[k.lower()] = v
        return type.__new__(mcs, name, bases, new_dict)


class MyClass(object):
        __metaclass__ = MetaClass
        @classmethod
        def SayHello(cls):
            print("hello")

# Look! we now call the method in lowercase...
MyClass.sayhello()
