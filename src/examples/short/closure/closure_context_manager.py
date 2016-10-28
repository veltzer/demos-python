#!/usr/bin/python3

'''
This is a basic closure example.
'''

def iterate_it(filename): 
    with open(filename) as f:
        yield from f

def iter_through_files(filenames):
    l=[]
    for filename in filenames:
        l.append(iterate_it(filename))
    return l

iters=iter_through_files(['/etc/passwd','/etc/group'])
for i in iters:
    for l in i:
        print(l, end='')
