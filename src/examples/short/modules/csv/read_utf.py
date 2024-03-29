"""
This example shows how to read a csv utf file in python3 using the
built in "csv" module.

NOTES:
- what encoding does "open" open a file with if you do not pass an encoding?
- the answer is "locale.getpreferredencoding()"
- and what does that mean?
- well, on most systems it is utf-8 but sysadmins and even users can override that.
- for python, users can override this also using the PYTHONIOENCODING
environment variable.
- so whats the bottom line?
- if you want to be absolutely sure you are opening a file in utf-8 encoding,
pass it to "open" in python3 using the encoding parameter. if you do not pass
 the parameter then python will use locale.getprefferedencoding() to get the encoding
 which will probably be UTF-8.

References:
- https://docs.python.org/3/library/locale.html#locale.getpreferredencoding
- https://docs.python.org/3/library/functions.html#open
- https://www.python.org/dev/peps/pep-0540/
"""

import csv
import locale


print(locale.getpreferredencoding())

# open a regular file with the utf-8 encoding works
with open("data/csv/file.csv") as csv_file:
    r = csv.reader(csv_file)
    for row in r:
        pass

# now lets try reading a real utf file
with open("data/csv/file_utf.csv") as csv_file:
    r = csv.reader(csv_file)
    for row in r:
        pass

# now lets try reading a real utf file without the encoding
with open("data/csv/file_utf.csv") as csv_file:
    r = csv.reader(csv_file)
    for row in r:
        print(row)
