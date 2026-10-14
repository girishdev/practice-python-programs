"""Definition: A class is a blueprint for creating objects, and an object is an instance of a class.

Explanation:
A class describes what data an object should store and what actions it can perform.
Think of a class as a template, while an object is a real item created from that template.
In this example, Dog is the class, and dog1 and dog2 are two separate objects created from it.
"""


class Dog:
    # Class blueprint
    def __init__(self, name):
        self.name = name  # Instance attribute

    def bark(self):
        return f"{self.name} says woof!"


# Object creation
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print("Class and Object")
print(dog1.bark())
print(dog2.bark())
