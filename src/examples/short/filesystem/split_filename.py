#!/usr/bin/env python

"""
This example shows how to split a filename into its components.

NOTES:
- split is just like (dirname, basename)
- splitext is for extensions.
"""

import sys
import os.path

for line in sys.stdin:
    line = line.strip()
    print('basename is [{0}]'.format(os.path.basename(line)))
    print('dirname is [{0}]'.format(os.path.dirname(line)))
    print('splitext is [{0}]'.format(os.path.splitext(line)))
    print('split is [{0}]'.format(os.path.split(line)))
