"""
This is an example of how to use more than one context manager at a time...

References:
- https://stackoverflow.com/questions/893333/multiple-variables-in-a-with-statement
"""


class MyResource:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} constructor")

    def __enter__(self):
        print(f"{self.name} enter")

    def __exit__(self, _type, value, traceback):
        print(f"{self.name} exit")


with MyResource("r1") as r1, MyResource("r2") as r2:
    print("block of code")
