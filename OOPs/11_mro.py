"""Definition: MRO (Method Resolution Order) determines the order in which Python looks for methods in inheritance hierarchy.

Explanation:
MRO is the sequence Python uses to search for methods when multiple classes are involved in inheritance.
It helps Python resolve which implementation should be used when a method exists in more than one parent class.
Understanding MRO is important in complex inheritance structures.
"""


class A:
    def show(self):
        return "A"


class B(A):
    pass


class C(A):
    def show(self):
        return "C"


class D(B, C):
    pass


print("MRO")
print(D.__mro__)
print(D().show())
