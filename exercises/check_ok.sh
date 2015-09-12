#!/bin/sh

find . -mindepth 2 -type f -not -name "exercise.txt" -not -name "solution*.py" -not -name "data*.txt" -not -name "data.xml" -not -name "start.py" -not -name "myclass*.py"
