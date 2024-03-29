"""
This is an example of using a property in python.
- We store the value in the "real" attribute "__price".
- This attribute is "private" (well,mangled anyway...).
- This example also uncovers a bug in the python interpreter
which cashes the value of __price but does not do this for
the magical "x.price" property.
- This idea is similar to ideas in languages such as C#.
"""


class Book:
    def __init__(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setPrice(self, val):
        self.__price = val

    price = property(getPrice, setPrice)

    def print_via_prop(self):
        print("printMe: price is", self.price)

    def print_via_direct(self):
        print("printMe: price is", self.__price)

    def print_via_get(self):
        print("printMe: price is", self.getPrice())


print("this is the type(Book.price)", type(Book.price))
b = Book(50)
print("this is dir(instance)", dir(b))
b.print_via_prop()
b.print_via_direct()
b.print_via_get()
print("b.price is", b.price)
b.price = 60
b.print_via_prop()
b.print_via_direct()
b.print_via_get()
print("b.price is", b.price)
