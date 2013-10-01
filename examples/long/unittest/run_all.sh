#!/bin/sh

for x in `find . -name "*Test.py"`; do
	echo $x
	$x
done
