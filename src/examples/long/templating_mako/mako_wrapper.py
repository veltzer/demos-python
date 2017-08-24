#!/usr/bin/env python

import datetime
import sys

import mako.lookup


def years(x):
    curr_year = datetime.datetime.now().year
    return ','.join(map(str, range(x, curr_year + 1)))


d = {
    'a': 'b',
    'c': 'd',
}

if len(sys.argv) != 3:
    print(sys.argv[0] + ': usage: ' + sys.argv[
        0] + ' [input] [output]', file=sys.stderr)
    sys.exit(1)

input_encoding = 'utf-8'
output_encoding = 'utf-8'
p_input = sys.argv[1]
p_output = sys.argv[2]

mylookup = mako.lookup.TemplateLookup(
    directories=['.'], input_encoding=input_encoding, output_encoding=output_encoding)
template = mako.template.Template(
    filename=p_input, lookup=mylookup, output_encoding=output_encoding, input_encoding=input_encoding)
# the order here is importat. Do not open the file for writing until the rendering
# is complete since we want to make sure that the rendering process does not throw
# an exception. Only then do we open the file for writing.
# otherwise we will leave behind a partially written file and force the user
# to fix his makefile to remove the cruft we left behind...
output = template.render(foo='bar', years=years, d=d)
file = open(p_output, 'wb')
file.write(output)
file.close()
# os.chmod(p_output, 0o0444)
