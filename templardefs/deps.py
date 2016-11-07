'''
dependencies for this project
'''

opt_python_version='3.5'

def populate(d):
    d.packs=[
        # python core
        'python3',
        'python3-doc',
        'python3-examples',
        'python{0}'.format(opt_python_version),
        'python{0}-doc'.format(opt_python_version),
        'python{0}-examples'.format(opt_python_version),
        'python{0}-dev'.format(opt_python_version),
        'python{0}-venv'.format(opt_python_version),

        # iteractive, parallel python
        'ipython3',

        # tools for python packaging and upload
        'twine',

        # qt
        'pyqt4-dev-tools',
        'python3-pyqt4',
        'python3-dbus.mainloop.qt',

        # curses
        'python3-newt',
        'python3-dialog',

        # misc modules
        'python3-mysql.connector',
        'python3-progressbar',
        'python3-networkx', # tool to create, manipulate and study complex networks (Python3)
        'python3-pygraph', # library for working with graphs in Python (Python3)
        'python-yapsy-doc', # simple plugin system for Python applications doc
        'python3-yapsy', # simple plugin system for Python3 applications
        'python3-pygments', # for syntaxh highlighting
        'python3-jinja2', # for jinja templating

        # mako
        'python3-mako', # for mako templating
        'python-mako-doc', # documentation for mako templating

        # debuggers
        'winpdb',
        'pydb',
        'python3-pudb',

        # sphinx
        'python3-sphinx', # documentation generator for Python projects (implemented in Python 3)
        'python3-sphinx-paramlinks', # allows param links in Sphinx function/method descriptions to be linkable
        'python3-sphinxcontrib.programoutput', # insert the output of arbitrary commands into documents Python 3.x
        'python3-sphinxcontrib.spelling', # Sphinx spelling extension (Python 3)
        'python3-sphinxcontrib.youtube', # Sphinx YouTube extension

        # notify related packages
        'python3-notify2',
        'python-pyinotify-doc',
        'python3-pyinotify',

        # python and gtk stuff
        'glade',

        # lint and code formatting
        'python-autopep8',

        # pdf creation with python
        'python3-pypdf2',

        # web scraping
        'python3-requests',

        # logging tree
        'python3-logging-tree',

        # click
        'python3-click',

        # boto
        'python3-boto',
        'python3-boto3',
    ]
    d.requirements3=[
        'signalfd',
        'luigi',
        'scrapy',
        'unidecode',
        'click',
        'pandas',
        'pyyaml',
    ]

def getdeps():
    return [ __file__ ]
