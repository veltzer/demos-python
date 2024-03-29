"""
http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html

*TL;DR
Separates an algorithm from an object structure on which it operates.

An interesting recipe could be found in
Brian Jones, David Beazley "Python Cookbook" (2013):
- "8.21. Implementing the Visitor Pattern"
- "8.22. Implementing the Visitor Pattern Without Recursion"

*Examples in Python ecosystem:
- Pythons ast.NodeVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L250
which is then being used e.g. in tools like `pyflakes`.
- `Black` formatter tool implements its own: https://github.com/ambv/black/blob/master/black.py#L718
"""


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = "visit_" + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *_args, **_kwargs):
        print("generic_visit " + node.__class__.__name__)

    def visit_B(self, node, *_args, **_kwargs):
        print("visit_B " + node.__class__.__name__)


EXPECTED_OUTOUT = """
generic_visit A
visit_B B
visit_B C
"""


def main():
    c = C()
    print(c.__class__.__mro__)
    a, b, c = A(), B(), C()
    visitor = Visitor()
    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)


if __name__ == "__main__":
    main()
