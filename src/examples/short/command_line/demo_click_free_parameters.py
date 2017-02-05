#!/usr/bin/python3

"""
This demo shows how to create a click program that accepts many free
paramters on the command line.

References:
- http://click.pocoo.org/5/arguments/#variadic-arguments
"""

import click


@click.command()
@click.argument('args', nargs=-1)
def hello(args):
    """Simple program that greets NAME for a total of COUNT times."""
    print(args)


if __name__ == '__main__':
    hello()
