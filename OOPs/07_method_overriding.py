"""Definition: Method overriding happens when a subclass provides a different implementation of a method already defined in its parent class.

Explanation:
Overriding lets a child class change the behavior inherited from its parent.
This is useful when the child needs a more specific version of a method.
In this example, Cat replaces the general Animal.sound() behavior with its own version.
"""


class Animal:
    def sound(self):
        return "Animal sound"


class Cat(Animal):
    def sound(self):
        return "Meow"


print("Method Overriding")
print(Cat().sound())
