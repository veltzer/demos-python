#!/usr/bin/python3

"""
This example explores loading/saving dictionaries in python from/to files

Notes:
- python sets are not JSON serializable
"""

import json  # for dump, load
import sys  # for exit

my_dict = {
    'one': 'onev',
    'two': 'twov',
}
my_set = {
    'one',
    'two',
}

filename = '/tmp/json_store.json'

with open(filename, 'w') as f:
    json.dump(my_dict, f, indent=4)
    try:
        json.dump(my_set, f)
        sys.exit(1)
    except:
        pass

with open(filename) as f:
    other_dict = json.load(f)

print(other_dict)
