#!/usr/bin/python3

'''
This example shows how to remove a folder with all of its subfolders in
python using the shutil package.

NOTES:
the folder must exist. If you want a softer solution then look at
the rmtree_if_exists function below...
'''

import shutil # for rmtree
import os.path # for isdir

def rmtree_if_exists(folder):
	if os.path.isdir(folder):
		shutil.rmtree(folder)

shutil.rmtree('/tmp/folder_to_remove')
