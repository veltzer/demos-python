"""
This example shows how to count using a dictionary
"""

import collections

colors = [
    "red",
    "green",
    "red",
    "blue",
    "green",
    "red",
]

# the simple way
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)

# shorter code
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

# with collections.defaultdict
d = collections.defaultdict(int)
for color in colors:
    d[color] += 1
print(d)

# with collections.Counter
d = collections.Counter(["red", "green"])
# this is how to do a single update
d["green"] += 1
# this is how to do a multi update
d.update(["red", "green"])
print(d)
