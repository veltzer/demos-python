"""
This is an example of creating your own resource to be used with the "with"
python syntax. This is called a "Context Manager".

You can see the basic flow of code:
- first the constructor of your context manager is called.
- then your __enter__ code is called.
- then the users code block is executed.
- then your __exit__ code is called.
"""


class MyResource:

    def __init__(self):
        print("constructor")

    def __enter__(self):
        print("enter")

    def __exit__(self, exception_type, value, traceback):
        if value is not None:
            print("there was an exception")
            print(f"exception_type is {exception_type}")
            print(f"{value}")
            print(f"{type(value)}")
            print(f"{traceback}")
        else:
            print("there was no exception")


print("lets see a basic use of the context manager...")
with MyResource():
    print("block of code")
    raise ValueError(7)
