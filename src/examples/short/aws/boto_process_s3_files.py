"""
An example about how to connect to s3 and iterate files
in some "sub folder" of s3.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.

References:
- http://boto.cloudhackers.com/en/latest/
- http://boto.cloudhackers.com/en/latest/ref/
"""

import boto

do_count_lines = True
do_print = True

bucket_name = "bucket_name"
folder = "folder"

conn = boto.connect_s3()
bucket = conn.get_bucket(bucket_name)
key_list = bucket.list(folder)
file_num = 0
for key in key_list:
    print('doing [{0}]'.format(key.name))
    file_num += 1
    if do_count_lines:
        key.open_read()
        line_number = 0
        for line in key:
            if do_print:
                print(line, end='')
            line_number += 1
        print('got [{0}] lines...'.format(line_number))
print('got [{0}] files...'.format(file_num))
