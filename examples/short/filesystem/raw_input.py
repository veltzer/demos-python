#!/usr/bin/python

'''
This is an example of how to read data from the user on the console.

Notice that:
- When you get data from 'raw_input' it is always a string.
- You can convert it to 'int' or 'float' using regular contrcutors
but there is a chance that they will throw an exception.
- At the end of the string given to 'raw_input' you *do* need a space since
raw input prints to the screen * exactly * what you give it...
'''

text=raw_input('please give me a number: ')
print(type(text))
val=int(text)
print('val is',val)
print('type(val) is',type(val))
