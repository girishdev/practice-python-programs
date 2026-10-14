"""Definition: Instance methods use self, class methods use cls, and static methods do not depend on the instance or class.

Explanation:
Instance methods work with a specific object and can access its data through self.
Class methods work with the class itself and receive cls as a parameter.
Static methods do not depend on either self or cls and are useful for utility functions.
"""


class Calculator:
    def instance_method(self, a, b):
        return a + b

    @classmethod
    def class_method(cls, a, b):
        return a * b

    @staticmethod
    def static_method(a, b):
        return a - b


calc = Calculator()
print("Instance, Class, and Static Methods")
print(calc.instance_method(3, 4))
print(Calculator.class_method(3, 4))
print(Calculator.static_method(10, 4))
