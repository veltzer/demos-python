#!/usr/bin/python3

import plugin_mgr # for importPlugins, importPlugin

# the easiest way to use
plugins=plugin_mgr.importPlugins(folder='plugins')

print(plugins.plugin1)

#plugin_mgr.importPlugins(folder='plugins', ns='plugins')

#plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2' ], 'plugin1')
#plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2' ], 'plugin2')
