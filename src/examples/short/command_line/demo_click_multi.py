#!/usr/bin/python3

'''
A demo of how to do multi commands in click
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
