#!/bin/sh

find . -mindepth 2 -type f -not -name "exercise.txt" -not -name "solution.py" -not -name "solution1.py" -not -name "solution2.py" -not -name "data.txt" -not -name "data.xml"
