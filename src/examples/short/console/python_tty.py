#!/usr/bin/python3

'''
This example shows /dev/tty and standard streams.
'''

import sys  # for stdout, stderr

print('Hello from regular print')
print('Hello from sys.stdout', file=sys.stdout)
print('Hello from sys.stderr', file=sys.stderr)

sys.stdout.close()

# these will cause an exception
# print('Where did this go?')
# print('Where did this go?', file=sys.stdout)

with open('/dev/tty', 'w') as f:
    f.write('Hello from /dev/tty...\n')
    f.flush()
