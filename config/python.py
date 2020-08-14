import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

run_requires = [
    'click',
    'requests',
    'tqdm',
    'cmd2',
    'pythondialog',
    'lmdb',
    'cachetools',
    'pandas',
    'dispy',
    'mako',
    'luigi',
    'pyinotify',
    'twisted',
    'yapsy',
    'pymysql',
    'mysql.connector',
    'sqlalchemy',
    'plotly',
    'gcloud',
    'networkx',
    'keyring',
    'dbus-python',
    'python-jenkins',
    'SortedContainers',
    'PyRSS2Gen',
    'fire',
    'PyGithub',
    'prompt-toolkit',
    'PyQt5',
    'azure-cognitiveservices-search-websearch',
    'pygraph',
    'music',
    'flask',
    'tsv',
    'psycopg2',
    'pygments',
    'simpleparse',
    # gtk stuff
    # 'pycairo',
    # 'PyGObject',
]

test_requires = [
]

dev_requires = [
    'pydmt',  # for building
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.5"
