# CHECK_WITH python2

print('[{0}] loading'.format(__file__))

import yapsy.IPlugin


class PluginOne(yapsy.IPlugin.IPlugin):

    def __init__(self):
        print('This is plugin 1 __init__')

    def print_name(self):
        print('This is plugin 1')

var = 'plugin1_value'

extra_var_only_for_plugin1 = 'extra_value_only_for_plugin1'
