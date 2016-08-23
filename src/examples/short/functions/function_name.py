#!/usr/bin/python3

'''
This example shows how to find a function name as a string

We show how to find the function name from:
- within the function (sys._getframe().f_code.co_name)
- outside the function (myfunc.__name__)

References:
- http://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
'''

import sys

def myfunc():
    this_function_name = sys._getframe().f_code.co_name
    print(this_function_name)

print(myfunc.__name__)
print(myfunc.__qualname__)
print(myfunc.__module__)
myfunc()
#print(dir(myfunc))
