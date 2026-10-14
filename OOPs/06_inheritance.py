"""Definition: Inheritance allows a class to reuse attributes and methods from another class.

Explanation:
Inheritance creates an "is-a" relationship between classes.
A child class inherits features from a parent class, which reduces duplicate code and promotes reusability.
Here, Dog inherits from Animal and uses the parent class structure while adding its own behavior.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


print("Inheritance")
dog = Dog("Buddy")
print(dog.speak())
