#!/usr/bin/python3

"""
This example demonstrates how to show the default value for a paramter
in click.

The parameters:
    show_default,
    help,
    type,
as NOT allowed for the free arguments section (click.argument).
"""

import click


@click.command()
@click.option(
        '--count',
        default=1,
        type=int,
        help='Number of greetings.',
        show_default=True,
)
@click.argument(
        'args',
        nargs=-1,
)
def main(count, args):
    """ simple demo that shows default values """
    print(count)
    print(args)


if __name__ == '__main__':
    main()
