import imp # for find_module, load_module
import os # for listdir
import os.path # for join, isfile

def load_module(module_ns, name, folder):
	info=imp.find_module(name, [folder])
	return imp.load_module(module_ns, *info)

def importPlugins(folder=None, ns=None):
	if ns is None:
		ns=folder
	files=os.listdir(folder)
	l=[]
	for file in files:
		if file.endswith('.py'):
			name=file[:-3]
			module_ns=os.path.join(ns, name)
			m=load_module(module_ns, name, folder)
			l.append((name,module_ns,m))
	return l

'''
This one imports a single plugin by name from a path giving path precedence
'''
def importPlugin(ns, path, name):
	for path_elem in path:
		test_file=os.path.join(path_elem, name+'.py')
		if os.path.isfile(test_file):
			load_module(ns, name, path_elem)
			return
	raise ValueError('plugin '+name+' not found')
