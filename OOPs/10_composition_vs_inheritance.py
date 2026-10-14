"""Definition: Composition builds objects using other objects, while inheritance creates a subclass relationship.

Explanation:
Composition means a class contains another object and uses it to perform work.
Inheritance means one class extends another and inherits its behavior.
Composition is often preferred when objects are made of parts, such as a Car having an Engine.
"""


class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        return self.engine.start()


print("Composition")
print(Car().drive())
