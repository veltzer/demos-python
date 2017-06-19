"""
This is a module that checks if a library given to it is loadable
(has no undefined references)
"""

import ctypes
import ctypes.cdll

libdl = ctypes.CDLL('libdl.so')
lib = None


def check_lib(name):
    l = ctypes.cdll.LoadLibrary(name)
    # noinspection PyProtectedMember
    libdl.dlclose(l._handle)


def load_lib(name):
    global lib
    lib = ctypes.cdll.LoadLibrary(name)
