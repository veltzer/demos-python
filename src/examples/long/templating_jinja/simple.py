#!/usr/bin/python3

import jinja2

t=jinja2.Template("Hello {{ something }}!")
print(t.render(something="World"))
