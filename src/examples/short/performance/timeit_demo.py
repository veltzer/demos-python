#!/usr/bin/python3

'''
Example of timing python code using the 'timeit' module

Why should you use this module and not time everything yourself?
Well, if you time things yourself you must be very careful to:
- use process/thread time and not clock time
- turn off garbage collection so that it wont soil your measurements
and other pitfalls.

I haven't really made sure that the 'timeit' module really does
all of these properly but it is supposed to.

You can use the 'timeit' module from the command line like this:
python -m timeit -s 'text = "sample string"; char = "g"'  'char in text'
'''

import timeit  # for timeit

print(timeit.timeit('\'-\'.join(str(n) for n in range(100))', number=10000))
