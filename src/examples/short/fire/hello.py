#!/usr/bin/env python

# https://google.github.io/python-fire

import fire

def hello(name="World"):
    return "Hello %s!" % name

if __name__ == '__main__':
    fire.Fire(hello)