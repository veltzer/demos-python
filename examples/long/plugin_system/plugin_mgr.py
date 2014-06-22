import imp # for find_module, load_module
import os # for listdir
import os.path # for join, isfile

def load_module(ns, name, folder):
	info=imp.find_module(name, [folder])
	imp.load_module(ns, *info)

def importPlugins(ns, folder):
	possibleplugins=os.listdir(folder)
	for f in possibleplugins:
		location=os.path.join(folder, f)
		if location.endswith('.py'):
			load_module(ns, f[:-3], folder)

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
