Write a script that shows a file in a tabular format.
Here is an example of a file:
=========>8=============
Mark Python 8
Doron Java 5
=========>8=============
The output should be like this:
Mark  Python 8
Doron Java   5
Note that:
- the output is tabular
- the widths of the columns were calculated to match the data.

What do you need to do?
Read the values in the original table and "pad" them with spaces
Your script should read the data from standard input and write its output to standard output.
Your script will be run like this:
./your_script.py < test_data.txt > output.txt

You may assume that the input file is fully tabular, meaning that all lines have *the exact* number of
elements in them, with no exceptions.

Hint:
You may want to use this small trick to help you:
	[0] * 6 = [0, 0, 0, 0, 0, 0]