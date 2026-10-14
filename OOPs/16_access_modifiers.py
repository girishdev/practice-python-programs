"""Definition: Access modifiers control how attributes and methods are accessed: public, protected, and private.

Explanation:
In Python, public attributes are intended for normal access, protected attributes use a single underscore convention, and private attributes use a double underscore to limit direct access.
These conventions help keep data safe and make class design clearer.
This example shows how private data can still be accessed through controlled methods.
"""


class Person:
    def __init__(self, name, age, ssn):
        self.name = name          # Public
        self._age = age           # Protected
        self.__ssn = ssn         # Private

    def get_private_info(self):
        return self.__ssn


person = Person("Riya", 25, "123-45-6789")
print("Access Modifiers")
print(person.name)
print(person._age)
print(person.get_private_info())
