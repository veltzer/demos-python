"""
This example shows how to create a zip file in python using
the built in python module "zipfile"

References:
- https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
"""

import zipfile

with zipfile.ZipFile("/tmp/demo.zip", "w", zipfile.ZIP_DEFLATED) as zipfile_handle:
    # add a file to the archive, name in the archive will be the full
    # name of the file
    zipfile_handle.write("/etc/passwd")
    # add a file with a different name
    zipfile_handle.write(
        filename="/etc/group",
        arcname="this_is_groups",
    )
    # add a string as content
    zipfile_handle.writestr(
        zinfo_or_arcname="str",
        data="this is my data"
    )
