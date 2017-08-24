import base

print('[{0}] loading'.format(__file__))

var = 'plugin1_value'

extra_var_only_for_plugin1 = 'extra_value_only_for_plugin1'


def do_something():
    print('[{0}] running'.format(__file__))


class Plugin1(base.BaseClass):
    def __init__(self):
        print('in init of Plugin1')
