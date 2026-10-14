"""Definition: Abstraction hides implementation details and shows only essential features.

Explanation:
Abstraction focuses on what an object does rather than how it does it.
Abstract classes define a common interface, while subclasses provide the actual implementation.
This is useful when you want to standardize behavior across different classes.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


print("Abstraction")
print(Rectangle(4, 5).area())
