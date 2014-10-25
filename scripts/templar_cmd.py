#!/usr/bin/python3

'''
templating solution for this project
'''

import templar.cmdline # for cmdline
import attr # for Attr

templar.cmdline.cmdline({'attr':attr.Attr})
