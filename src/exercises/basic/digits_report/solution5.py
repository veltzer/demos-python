"""
This is a solution using a dictionary
"""

d = {}
for i in range(10):
    d[i] = 0

s = input("Please enter a line of digits: ")
for c in s:
    if c.isdigit():
        d[int(c)] += 1
    else:
        print("you moron")

for i in range(10):
    print(f"{i} appeared {d[i]} times in the text")
