""" plugin3.py """

print(f"[{__file__}] loading")

var = "plugin1_value"

extra_var_only_for_plugin1 = "extra_value_only_for_plugin1"


def do_something():
    print(f"[{__file__}] running")
