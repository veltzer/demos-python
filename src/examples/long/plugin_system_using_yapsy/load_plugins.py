#!/usr/bin/python3

'''
This is an example of using yapsy to create a lightweight plugin based system.

References:
http://yapsy.sourceforge.net
'''

import yapsy.PluginManager

simplePluginManager = yapsy.PluginManager.PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(['plugins'])

print(
    'load all the plugins (this also calls the construction of IPlugin objects)')
simplePluginManager.collectPlugins()

print('now printing plugins info')
for pluginInfo in simplePluginManager.getAllPlugins():
    print('name is [{0}]'.format(pluginInfo.name))
    print('description is [{0}]'.format(pluginInfo.description))

print('activate all the plugins. I really dont know what this means')
for pluginInfo in simplePluginManager.getAllPlugins():
    simplePluginManager.activatePluginByName(pluginInfo.name)

print('do something with all plugins')
for pluginInfo in simplePluginManager.getAllPlugins():
    pluginInfo.plugin_object.print_name()
