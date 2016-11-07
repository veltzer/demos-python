#!/usr/bin/python3

'''
This is an example which shows a stadard dictionary vs an ordered dict.
'''

import collections # for OrderedDict

ud=dict()
od=collections.OrderedDict()
for i in range(10):
    ud[str(i)]=i
    od[str(i)]=i
print('unordered dict')
print(' '.join(['{k},{v}'.format(k=k,v=v) for k,v in ud.items()]))
print('ordered dict')
print(' '.join(['{k},{v}'.format(k=k,v=v) for k,v in od.items()]))