import demo


print('[{0}] loading'.format(__file__))

var = 'plugin2_value'

extra_var_only_for_plugin2 = 'extra_value_only_for_plugin2'


def do_something():
    print('[{0}] running'.format(__file__))


class Plugin2Class1(dict):
    pass


class Plugin2Class2(demo.BaseClass):
    pass
