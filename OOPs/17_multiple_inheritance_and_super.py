"""Definition: Multiple inheritance allows a class to inherit from more than one parent class, and super() calls the parent implementation.

Explanation:
Multiple inheritance means one class can inherit features from more than one parent class.
This can be powerful, but it must be used carefully because it can make method resolution more complex.
super() helps call the next class in the inheritance chain in a clean and maintainable way.
"""


class A:
    def show_a(self):
        return "Class A"


class B:
    def show_b(self):
        return "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def show_all(self):
        return f"{self.show_a()} and {self.show_b()}"


print("Multiple Inheritance and super()")
print(C().show_all())
