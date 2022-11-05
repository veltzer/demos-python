make_requires = [
    "pymakehelper",
    "pydmt",
]
dev_requires = [
    "black",
]
install_requires = [
    "click",
    "requests",
    "tqdm",
    "cmd2",
    "pythondialog",
    "lmdb",
    "cachetools",
    "psutil",

    "jsonschema",
    "dispy",
    "mako",
    "luigi",
    "pyinotify",
    "twisted",
    "yapsy",
    "pymysql",
    "mysql.connector",
    "sqlalchemy",
    "plotly",
    "gcloud",
    "networkx",
    "keyring",
    "python-jenkins",
    "SortedContainers",
    "PyRSS2Gen",
    "fire",
    "PyGithub",
    "gitpython",
    "prompt-toolkit",
    "PyQt5",
    "PyQt5-stubs",
    "azure-cognitiveservices-search-websearch",
    "pygraph",
    "flask",
    "tsv",
    "pygments",
    # "simpleparse", causing problems
    "progressbar",
    "inject",
    "scrapy",
    "ConfigParser",
    "unidecode",
    "bitmath",
    "paramiko",
    "boto",
    "boto3",
    "boto3-stubs",
    "attr",
    "pyparsing",
    "fastparquet",
    "logging_tree",
    "pluginbase",
    "reportlab",
    "imdbpy",
    "python-pptx",
    # selenium stuff
    "webdriver-manager",
    "selenium",
    "selenium-wire",
    # music
    "music",
    "mingus",
    # my stuff
    "pyapikey",
    "pyfakeuse",
    "pyvardump",
    # gtk stuff
    # "vext",
    # "vext.gi",
    # machine learning
    "pandas",
    "numpy",
    "furl",

    # There packages require special attention (they do not install without issues)
    "psycopg2",
    # TODO: cannot install because libsystem-dev cannot be installed
    # "systemd-python",
    "PyGObject",
    "PyGObject-stubs",
    "dbus-python",
    # terminal color stuff
    "termcolor",
    "colored",
    # yaml
    "oyaml",
    "ruamel.yaml",
    # google cloud
    "google-api-python-client",
    "google-auth-httplib2",
    "google-auth-oauthlib",
    "google-cloud-datastore",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-flake8",
    "flake8",
    "pylogconf",
    "mypy",
    "types-PyYAML",
    "types-setuptools",
    "types-boto",
    "types-PyMySQL",
    "types-requests",
    "types-paramiko",
    "types-termcolor",
]
