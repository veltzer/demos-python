# CHECK_WITH python2

import pkg_resources

import os.path  # for dirname, join
import pkgutil  # for get_data

static_file_content = pkg_resources.resource_string(
    'mypack', 'static_file.html').decode()
print('static_file_content is [{0}]'.format(static_file_content))


def get_real_filename(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def get_data(filename):
    return open(get_real_filename(filename), 'rb').read()
static_file_content2 = get_data('static_file.html').decode()
print('static_file_content2 is [{0}]'.format(static_file_content2))

static_file_content3 = pkgutil.get_data('mypack', 'static_file.html').decode()
print('static_file_content3 is [{0}]'.format(static_file_content3))
