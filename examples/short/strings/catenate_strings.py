#!/usr/bin/python3

'''
This example explores how best to catenate strings in python.
'''

import timeit # for timeit

print(timeit.timeit('"".join(["a", "b", "c"])', number=10000))
print(timeit.timeit('s="a"+"b"+"c"', number=10000))
print(timeit.timeit('s="a"; s+="b"; s+="c"', number=10000))
