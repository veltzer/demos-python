#!/usr/bin/python3

"""
This example shows that two activations of the gzip library to compress files
actually produce files with different md5 signatures.

The reason for this is the filename, date and compression levels.
You can control this by uding the GzipFile object which has more
parameters. This is not yet demonstrated in this demo.
"""

import hashlib
import gzip

f_name = '/etc/passwd'
output_template = '/tmp/test{}.gz'

for x in range(0,3):
    input_handle = open(f_name, 'rb')
    output_filename = output_template.format(x)
    myzip = gzip.open(output_filename, 'wb')
    block_size = 4096
    try:
        print('zipping {}'.format(output_filename))
        for chunk in iter(lambda: input_handle.read(block_size), b''):
            myzip.write(chunk)
    finally:
        input_handle.close()
        myzip.close()

    md5 = hashlib.md5()
    print('hashing {}'.format(output_filename))
    with open(output_filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)

    print(md5.hexdigest())
