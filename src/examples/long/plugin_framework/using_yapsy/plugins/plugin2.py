""" plugin2.py """

import yapsy.IPlugin

print(f"[{__file__}] loading")


class PluginTwo(yapsy.IPlugin.IPlugin):
    def __init__(self):
        super().__init__()
        print(f"This is __init__ of {__name__} {self}")

    # def activate(self):
    #     print(f"{__name__} is activated")

    def deactivate(self):
        print(f"{__name__} is deactivated {self}")

    def do_something(self):
        print(f"do_something for {__name__} {self}")


var = f"my variable value is [{__name__}]"
