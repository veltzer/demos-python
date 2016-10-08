#!/usr/bin/python3

'''
This example shows how to compare dictionaries

Note that in earlier version of python there was a 'cmp'
function that compared dictionaries which is now gone.
use the '==' operator instead.
'''

dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print(dict1==dict2)
print(dict2==dict3)
print(dict1==dict4)
