#!/usr/bin/env python

import sys
import codecs

# print(sys.stdout.encoding)
# sys.exit(0)

# you need these two lines for redirection to work
if sys.stdout.encoding is None:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
# or this:
# $ export PYTHONIOENCODING=UTF-8
# in the environment

data = u'\xe9'
print(data)
try:
    print('this is data {}'.format(data))
except UnicodeEncodeError:
    print("yes, got exception")
print(u'this works ok {}'.format(data))
