#!/usr/bin/env python

"""
An example of writing parquet files with 'fastparquet'.

References:
- https://github.com/dask/fastparquet
"""

from fastparquet import write

import pandas

df = pandas.read_csv("/etc/passwd", sep=":")

# this is uncompressed write (I think!)
write('/tmp/file.parq', df)
# this is compressed write
write('/tmp/file_compressed.parq', df, compression='GZIP', file_scheme='hive')
