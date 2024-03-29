"""
This is an example of comparing the performance of list vs tuple vs
set vs frozenset
"""

import timeit

n = 1000
repetitions = 1
x = [str(k) for k in range(n)]
s = set(x)
f = frozenset(x)
t = tuple(x)


def demo_list():
    return [value in x for value in x]


def demo_set():
    return [value in s for value in x]


def demo_frozenset():
    return [value in f for value in x]


def demo_tuple():
    return [value in t for value in x]


print(f"list {timeit.timeit(demo_list, number=repetitions):.04f}")
print(f"set {timeit.timeit(demo_set, number=repetitions):.04f}")
print(f"frozenset {timeit.timeit(demo_frozenset, number=repetitions):.04f}")
print(f"tuple {timeit.timeit(demo_tuple, number=repetitions):.04f}")
