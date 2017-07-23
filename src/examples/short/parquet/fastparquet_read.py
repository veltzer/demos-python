#!/usr/bin/env python

"""
An example of reading parquet files with 'fastparquet'.

References:
- https://github.com/dask/fastparquet
"""

from fastparquet import ParquetFile
import pandas

#pf = ParquetFile('/tmp/file.parq')
pf = ParquetFile('/tmp/file_compressed.parq')
df = pf.to_pandas()
print(df)
