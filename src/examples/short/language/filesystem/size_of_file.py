"""
This is a simple example that shows how to get the size of file in python.

References:
- https://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python
"""

import os

statinfo = os.stat("/etc/passwd")
print(f"size of the file is [{statinfo.st_size}]")
