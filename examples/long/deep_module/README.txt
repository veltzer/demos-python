This is a demo of how module initialization work.

things to note:

- when you run this you get this output:
hello from outer
hello from inner
hello from the module itself
hello from the module user
which clearly shows the order of initializers.

- if you remove either of the __init__.py then the example stops working.
	Conclustion: put a __init__.py in every module directory
	(you can actually try this on the cmd line).

- module usage is logical (import outer.inner.mod) instead of physical:
	outer/inner/mod.py. that is very good because:
	- you can write module loaders that load from other sources than
	the file system.
	- you can override file location using PYTHONPATH.
