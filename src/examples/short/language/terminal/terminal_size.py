"""
A program that shows you how to get the size of the terminal.

A clear winner in terms of performance is the ioctl(2) one.

References:
http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
"""

import fcntl
import os
import struct
import termios
import timeit


function_names = {}


def terminal_size1():
    h, w, _hp, _wp = struct.unpack("HHHH", fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0)), )
    return w, h


function_names[terminal_size1] = "ioctl"


def terminal_size2():
    ret = os.popen("stty size").read().split()
    return int(ret[1]), int(ret[0])


function_names[terminal_size2] = "stty"


def terminal_size3():
    x = int(os.popen("tput cols").read())
    y = int(os.popen("tput lines").read())
    return x, y


function_names[terminal_size3] = "tput"


def terminal_size4():
    d = {}
    for tc_entry in os.environ["TERMCAP"].split(":"):
        if tc_entry.find("#") != -1:
            key, val = tc_entry.split("#")
            d[key] = val
    return int(d["co"]), int(d["li"])


function_names[terminal_size4] = "TERMCAP"


def terminal_size5():
    """ this function does not work since LINES and COLUMNS are not exported"""
    x = int(os.environ["LINES"])
    y = int(os.environ["COLUMNS"])
    return x, y


function_names[terminal_size5] = "environment"

print(terminal_size1())
print(terminal_size2())
print(terminal_size3())
print(terminal_size4())
# print(terminal_size5())

functions = [
    terminal_size1,
    terminal_size2,
    terminal_size3,
    terminal_size4,
    #    terminal_size5,
]

number = 1000
results = [(timeit.timeit(f, number=number), function_names[f]) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print(f"{r[0]:.4f}: {r[1]}")
