#!/usr/bin/python3

"""
This example shows how to use the 'fetchmany' api of the cursor of psycopg2.

References:
- https://www.python.org/dev/peps/pep-0249/#arraysize
"""

import psycopg2

connection_string="postgresql://localhost/postgres"
with psycopg2.connect(connection_string) as connection:
    cursor = connection.cursor()
    print(cursor.arraysize)
    cursor.arraysize = 2
    cursor.execute("select * from test")
    while True:
        print('loop')
        rows = cursor.fetchmany()
        if not rows:
            break
        for row in rows:
            print(row)
