#!/usr/bin/python3

"""
A Demo for click

References:
- http://click.pocoo.org/5
"""

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--required', required=True, help='this is a required parameter')
@click.option('--output', required=True, help='output file', type=click.File('w', lazy=False))
@click.option('--hash-type', required=True, type=click.Choice(['md5', 'sha1']))
def hello(count, name, required, output, hash_type):
    """Simple program that greets NAME for a total of COUNT times."""
    print(required)
    print(output)
    print(hash_type)
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
