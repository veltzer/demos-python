print('[{0}] loading'.format(__file__))

import yapsy.IPlugin

class PluginFour(yapsy.IPlugin.IPlugin):
    def __init__(self):
        print('This is __init__ of {0}'.format(__name__))
    def activate(self):
        print('{0} is activated'.format(__name__))
    def deactivate(self):
        print('{0} is deactivated'.format(__name__))
    def do_something(self):
        print('do_something for {0}'.format(__name__))

var = 'my variable value is [{0}]'.format(__name__)