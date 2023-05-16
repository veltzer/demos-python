"""
A basic example of how to get a password from the default
keyring of you environment.
"""

import keyring
password = keyring.get_password("dummyapp", "mark.veltzer@gmail.com")
print(f"your password is [{password}]")
