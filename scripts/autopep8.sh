#!/bin/sh

<< COMMENT

- We may add "-a" or "-a -a" to the autopep8 to make it fix more.
- Use 'autopep8 --list-fixes' to see the list of things autopep8 does
- You can select exactly which fixes to apply and which to ignore.
- Currently we apply all fixes quite aggressively.

COMMENT

autopep8 -a -a -a -r -i src
