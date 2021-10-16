"""
This example shows that scope of variables in a python function
is really local
"""


# noinspection PyShadowingNames
def my_function():
    # pylint: disable=redefined-outer-name
    x = 5
    print(x)


x = 7
my_function()
print(x)
