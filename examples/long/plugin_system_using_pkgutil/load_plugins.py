#!/usr/bin/python3

'''
This is an example of using pkgutil to create a lightweight plugin based system.

TODO:
- list all properties of the new package
'''

import pkgutil

do_debug=False

for (module_loader, name, ispkg) in pkgutil.iter_modules(path=['plugins']):
	if do_debug:
		print(module_loader, name, ispkg)
	if not ispkg:
		m=module_loader.find_module(name)
		r=m.load_module()
		if do_debug:
			print(type(r))
			print(dir(r))
		print('var in that module is [{0}]'.format(r.var))
		print('members of [{0}]'.format(name))
		for p,v in r.__dict__.items():
			if not p.startswith('__'):
				print('\t{0} -> {1}'.format(p, v))
