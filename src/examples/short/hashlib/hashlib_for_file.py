#!/usr/bin/python3

"""
This is an example of how to use the python builtin 'hashlib' module
for calculating hash functions of file content.

References:
http://pythoncentral.io/hashing-files-with-python/
"""

import hashlib  # for new
import subprocess  # for check_output


def hex_digest(filename, algo):
    block_size = 65536
    hash_object = hashlib.new(algo)
    with open(filename, 'rb') as afile:
        buf = afile.read(block_size)
        while len(buf) > 0:
            hash_object.update(buf)
            buf = afile.read(block_size)
    return hash_object.hexdigest()


print(hashlib.algorithms_available)
print(hex_digest('/etc/passwd', 'sha512'))
print(subprocess.check_output(['sha512sum', '/etc/passwd']))
