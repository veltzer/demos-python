#!/usr/bin/python3

'''
An example about how to connect to s3 and iterate files
in some "subfolder" of s3 using the 'boto3' module.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.

References:
- https://boto3.readthedocs.io/en/latest/
'''

import boto3 # for connect_s3
import codecs # for getreader

do_count_lines=False

s3 = boto3.resource('s3')
bucket = s3.Bucket('twiggle-click-streams')
for key in bucket.objects.all():
    print('doing [{0}]'.format(key.name))
    file_num+=1
    if do_count_lines:
        wrapped_key = codecs.getreader('utf-8')(key)
        key.open_read()
        count=0
        for line in key:
            count+=1
        print('got [{0}] lines...'.format(count))
print('got [{0}] files...'.format(file_num))
