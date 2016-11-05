#!/usr/bin/python3

'''
A demo of how to do multi commands in click

TODO:
- add how to pass options to the subcommands and global options.
'''

import click

@click.group()
def cli():
    pass

@cli.command()
def say_hello():
    print('hello')

@cli.command()
def say_goodbye():
    print('goodbye')
