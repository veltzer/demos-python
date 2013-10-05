#!/usr/bin/python

import plugin_mgr # for importPlugins, importPlugin

plugin_mgr.importPlugins('plugins', 'plugins')

plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2' ], 'plugin1')
plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2' ], 'plugin2')
