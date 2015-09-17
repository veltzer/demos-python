#!/usr/bin/python3

'''
This example of how to wrap a dictionary to look like a namespace
'''


class D(dict):

    def __init__(self):
        pass

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, val):
        self[name] = val

a = D()
a['one'] = 'onev'
a.two = 'twov'

print(a['one'])
print(a.one)

print('listing all entries in the object')
for k, v in a.items():
    print(k, v)
