#!/usr/bin/python3

'''
A demo for the argparse which is arguably the best python
command line parsing module.

try this command to check it out:
./demo_argparse.py process --input in --output out

References:
https://docs.python.org/3/howto/argparse.html
https://docs.python.org/3/library/argparse.html#module-argparse
'''

import argparse # for ArgumentParser

parser=argparse.ArgumentParser()
subparsers=parser.add_subparsers(title='subcommands', dest='subcommand')
subparser_process=subparsers.add_parser('process')
subparser_process.add_argument('--input', help='input file')
subparser_process.add_argument('--output', help='output file')
subparser_process.add_argument('--chmod', help='chmod the output?', default=True, action='store_false')
subparser_print=subparsers.add_parser('print')
parser.add_argument('-d','--debug', help='debug the script', default=False, action='store_true')
parser.add_argument('-i','--integer', help='integer', type=int, default=5, choices=[5,7,9])
args=parser.parse_args()

print(args)
