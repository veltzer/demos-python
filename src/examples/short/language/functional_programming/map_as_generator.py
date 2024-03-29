"""
This example shows that in python3 map is a generator and does not return a list.
If you want to turn its output into a list there are two ways to do it:
- list
- [] (list comprehension)

Note that in python2.7 the behaviour was different.
"""


def generate_items():
    yield from range(10)


def square(x):
    return x ** 2


# wrong, still a generator
print(map(square, generate_items()))
# right, using the "list" function
print(list(map(square, generate_items())))
# right, using list comprehension
# pylint: disable=unnecessary-comprehension
print([x for x in map(square, generate_items())])
