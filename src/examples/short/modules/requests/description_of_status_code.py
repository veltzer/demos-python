"""
This example shows how to get the description of various http status codes using the "requests"
module.

Please note that this method is not advised as we are accessing a protected member of
the "requests" module which:
- may change in the future.
- created issues with development environments like pycharm which emit warnings on such shenanigans.

Better options would be to use the "http" module which is preinstalled in python 3.

References:
- https://stackoverflow.com/questions/24718557/get-the-description-of-a-status-code-in-python-requests
"""

import requests


def get_http_status_string(code: int):
    """
    This function returns a description of an HTTP status code (404 - not found etc).
    Unfortunately, the requests module does not provide a clean API for this so
    we must access a protected member (underscore member) of "requests.status_code".
    See:
    https://stackoverflow.com/questions/24718557/get-the-description-of-a-status-code-in-python-requests
    :param code:
    :return:
    """
    # noinspection PyProtectedMember,PyUnresolvedReferences
    # pylint: disable=protected-access
    return f"http code [{code}], [{requests.status_codes._codes[code][0]}]"  # type: ignore


url = "http://www.google.com/does_not_exist"
r = requests.get(url, timeout=5)
print(get_http_status_string(r.status_code))
