"""
This example shows that if you have a generator
you can turn it into a real list using several ways:
- list
- [] (list comprehension)

It also shows that the () comprehension will leave a generator
as a generator and the wrong ways of doing it...
"""


def generate_items():
    yield from range(10)


y = list(generate_items())
print(y)

# pylint: disable=unnecessary-comprehension
z = [x for x in generate_items()]
print(z)

# wrong examples
w1 = (x for x in generate_items())
print(w1)

w2 = generate_items()
print(w2)

w3 = [generate_items()]
print(w3)
