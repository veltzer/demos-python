#!/usr/bin/python3

'''
An example about how to connect to s3 and iterate files
in some "subfolder" of s3.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.
'''

import boto # for connect_s3
import codecs # for getreader

do_count_lines=False

conn = boto.connect_s3()
bucket = conn.get_bucket('twiggle-click-streams')
key_list = bucket.list('mft.similarweb.com')
file_num=0
for key in key_list:
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
