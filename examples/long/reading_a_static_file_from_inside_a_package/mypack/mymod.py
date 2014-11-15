import pkg_resources

static_file_content=pkg_resources.resource_string('mypack', 'static_file.html').decode()
print('static_file_content is [{0}]'.format(static_file_content))
