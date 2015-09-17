# CHECK_WITH python2

print('[{0}] loading'.format(__file__))

import yapsy.IPlugin


class PluginTwo(yapsy.IPlugin.IPlugin):

    def __init__(self):
        print('This is plugin 2 __init__')

    def print_name(self):
        print('This is plugin 2')

var = 'plugin2_value'

extra_var_only_for_plugin2 = 'extra_value_only_for_plugin2'
