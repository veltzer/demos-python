#!/usr/bin/env python

"""
this sys.path.append in the next section is needed since we didn't
'properly' install the module to /usr/share/python.
If we had this would not have been neccessary.
"""

import sys

sys.path.append('build/lib.linux-i686-2.7')

# noinspection PyPep8
import car

c = car.Car()
print(c)
c.printSelf()
c.setNumber(777)
print(c.getNumber())
