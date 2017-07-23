#!/usr/bin/env python

"""
This example explores loading/saving dictionaries in python from/to files

Notes:
- python sets are not JSON serializable
"""

import json
import sys

my_dict = {
    'one': 'onev',
    'two': 'twov',
}
my_set = {
    'one',
    'two',
}

filename = '/tmp/json_store.json'

with open(filename, 'w') as file_handle:
    json.dump(my_dict, file_handle, indent=4)
    try:
        json.dump(my_set, file_handle)
        sys.exit(1)
    except:
        pass

with open(filename) as file_handle:
    other_dict = json.load(file_handle)

print(other_dict)
